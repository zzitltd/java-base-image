"""The survey matrix: which vendor/java/os/flavor cells exist and how each image is obtained."""
from dataclasses import dataclass

JAVA = [17, 21, 25]
FLAVORS = ["jdk", "jre"]
VENDORS = ["oracle", "redhat", "microsoft", "corretto", "temurin", "zulu"]

# OS base image (pinned to the current stable release), package manager, apt codename.
OS = {
    "alpine": ("alpine:3.24", "apk", ""),
    "debian": ("debian:trixie-slim", "apt", "trixie"),
    "ubuntu": ("ubuntu:26.04", "apt", "resolute"),
    "al2023": ("amazonlinux:2023", "dnf", ""),
    "ubi9-minimal": ("registry.access.redhat.com/ubi9/ubi-minimal:latest", "microdnf", ""),
    "ubi9": ("registry.access.redhat.com/ubi9/ubi:latest", "dnf", ""),
    "ubi10-minimal": ("registry.access.redhat.com/ubi10/ubi-minimal:latest", "microdnf", ""),
    "ubi10": ("registry.access.redhat.com/ubi10/ubi:latest", "dnf", ""),
    "oraclelinux": ("container-registry.oracle.com/os/oraclelinux:9-slim", "microdnf", ""),
    "azurelinux": ("mcr.microsoft.com/azurelinux/base/core:3.0", "tdnf", ""),
}
# Which vendors are surveyed on which OS.
VENDOR_OS = {
    "oracle": ["oraclelinux"],
    "redhat": ["ubi9-minimal", "ubi9", "ubi10-minimal", "ubi10"],
    "microsoft": ["azurelinux"],
    "corretto": ["alpine", "debian", "ubuntu", "al2023"],
    "temurin": ["alpine", "debian", "ubuntu"],
    "zulu": ["alpine", "debian", "ubuntu"],
}

RPM_REPOS = {}  # id -> (name, baseurl, gpgkey); none of the current cells needs a third-party rpm repo
APT_REPOS = {  # id -> (key url, "<url> <suite> <component>" with {codename} = OS codename, extra apt.conf)
    "corretto": ("https://apt.corretto.aws/corretto.key", "https://apt.corretto.aws stable main", ""),
    "adoptium": ("https://packages.adoptium.net/artifactory/api/gpg/key/public",
                 "https://packages.adoptium.net/artifactory/deb {codename} main", ""),
    # Azul's CDN serves a Packages.gz that does not match the signed Release file; bz2 and plain are consistent
    "zulu": ("https://repos.azul.com/azul-repo.key", "https://repos.azul.com/zulu/deb stable main",
             '#clear Acquire::CompressionTypes::Order;\\nAcquire::CompressionTypes::Order { \"bz2\"; };'),
}


@dataclass
class Cell:
    vendor: str
    java: int
    os: str
    flavor: str
    method: str  # official | repo | none
    image: str = ""  # official: the vendor image
    repo: str = ""  # repo: key into APT_REPOS / RPM_REPOS, "" = the distro's own repo
    pkg: str = ""  # repo: package name
    note: str = ""  # none: why; otherwise a remark

    @property
    def name(self):
        return f"{self.vendor}-{self.java}-{self.os}-{self.flavor}"

    @property
    def base_image(self):
        return self.image if self.method == "official" else OS[self.os][0]

    @property
    def pm(self):
        return OS[self.os][1]

    @property
    def variants(self):
        return ["base", "updated"] if self.method == "official" else ["updated"]

    def tag(self, variant):
        return f"jbi/{self.name}:{variant}"


def resolve(vendor, j, os_, f):
    official = lambda image, note="": Cell(vendor, j, os_, f, "official", image=image, note=note)
    repo = lambda pkg, repo_id="": Cell(vendor, j, os_, f, "repo", repo=repo_id, pkg=pkg)
    none = lambda note: Cell(vendor, j, os_, f, "none", note=note)
    if vendor == "oracle":
        return official(f"container-registry.oracle.com/java/openjdk:{j}") if f == "jdk" else none("Oracle ships no JRE image")
    if vendor == "microsoft":
        return official(f"mcr.microsoft.com/openjdk/jdk:{j}-azurelinux") if f == "jdk" else none("Microsoft ships no JRE image or package")
    if vendor == "redhat":
        if os_.startswith("ubi10") and j == 17:
            return none("RHEL 10 ships OpenJDK 21 and 25 only")
        if os_.endswith("-minimal"):
            return official(f"registry.access.redhat.com/{os_[:-8]}/openjdk-{j}{'' if f == 'jdk' else '-runtime'}")
        return repo(f"java-{j}-openjdk-{'devel' if f == 'jdk' else 'headless'}")
    if vendor == "corretto":
        if os_ == "al2023":
            return official(f"amazoncorretto:{j}-al2023-{'jdk' if f == 'jdk' else 'headless'}")
        if f == "jre":
            return none("Corretto ships JDK packages only on Alpine, Debian and Ubuntu")
        if os_ == "alpine":
            return official(f"amazoncorretto:{j}-alpine3.24-jdk")
        return repo(f"java-{j}-amazon-corretto-jdk", "corretto")
    if vendor == "temurin":
        if os_ == "alpine":
            return official(f"eclipse-temurin:{j}-{f}-alpine-3.24")
        if os_ == "ubuntu":
            return official(f"eclipse-temurin:{j}-{f}-resolute")
        return repo(f"temurin-{j}-{f}", "adoptium")
    if vendor == "zulu":
        if os_ == "alpine":
            return official(f"azul-zulu:{j}-{f}-alpine3.23", "Docker Official Image; Azul pins Alpine 3.23")
        if os_ == "debian":
            return official(f"azul-zulu:{j}-{f}-debian13")
        return repo(f"zulu{j}-{f}", "zulu")
    raise ValueError(vendor)


def cells():
    return [resolve(v, j, o, f) for v in VENDORS for j in JAVA for o in VENDOR_OS[v] for f in FLAVORS]


class BaseCell(Cell):
    """A plain OS base image, measured like the Java cells (both variants)."""
    @property
    def name(self):
        return f"base-{self.os}"

    @property
    def variants(self):
        return ["base", "updated"]


def base_cells():
    return [BaseCell("os", 0, os_, "none", "official", image=img) for os_, (img, _, _) in OS.items()]
