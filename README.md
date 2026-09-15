# java-base-image

Repeatable survey of public Java container images. For each vendor, Java version, OS base and flavor it
builds the image, records size, exact OS and Java version and C library, and counts trivy findings, so
that a base image can be chosen from measured data rather than reputation.

## Scope

- **Java versions**: 17, 21, 25. **Flavors**: `jdk` and `jre`, where `jre` is the vendor's runtime-only
  package or image (`-runtime` at Red Hat, `-headless` at Amazon).
- **Vendors**: Oracle OpenJDK, Red Hat build of OpenJDK, Microsoft build of OpenJDK, Amazon Corretto,
  Eclipse Temurin, Azul Zulu.
- **OS bases**, pinned to the current stable release in `matrix.py`, and the vendors surveyed on each:

| OS | Base image | libc | Vendors |
|---|---|---|---|
| alpine | alpine:3.24 | musl | Corretto, Temurin, Zulu |
| debian | debian:trixie-slim | glibc | Corretto, Temurin, Zulu |
| ubuntu | ubuntu:26.04 | glibc | Corretto, Temurin, Zulu |
| al2023 | amazonlinux:2023 | glibc | Corretto |
| ubi9-minimal, ubi9, ubi10-minimal, ubi10 | registry.access.redhat.com/ubi{9,10}/ubi[-minimal] | glibc | Red Hat |
| oraclelinux | Oracle's own image only | glibc | Oracle |
| azurelinux | Microsoft's own image only | glibc | Microsoft |

Other combinations are deliberately not measured. Cells that a vendor does not serve at all (no JRE from
Oracle, Microsoft or Corretto outside Amazon Linux; no OpenJDK 17 on RHEL 10) are listed as
`not-available` with the reason. `python3 jbi.py matrix` prints the resolution.

## How each image is obtained

In order of preference:

1. **Official image** published by the vendor (`official`): Docker Official Images for Temurin,
   Corretto and Zulu, the Red Hat, Oracle and Microsoft registries for theirs.
2. **Vendor package repository** on the plain OS base (`repo`): apt repos of Corretto, Adoptium and
   Azul on Debian and Ubuntu, the UBI AppStream repo for Red Hat on the standard UBI images.
3. **Vendor tarball** on the plain OS base (`tarball`): last resort, currently needed by no cell.

Repository quirks handled by the generated Dockerfiles: Debian and Ubuntu slim images lack
`ca-certificates`, so it is installed before any https repo is added; Azul's apt CDN serves a
`Packages.gz` that does not match the signed Release file, so apt is told to use the bz2 index for that
repo; Amazon Linux 2023 images lock to a repository snapshot, so the upgrade runs with
`--releasever=latest`.

## What is measured

Four kinds of image, each with uncompressed and compressed size, OS and libc version, and trivy counts:

1. **Base OS image** as published (`base-os.csv`, variant `base`).
2. **Updated OS image**: the same with all packages upgraded (`base-os.csv`, variant `updated`).
3. **Java image as published**: the official image untouched (`summary.csv`, variant `base`; official
   cells only).
4. **Java-enabled updated OS image**: the official image with its OS packages upgraded, or the OS base
   upgraded and Java installed from the repo (`summary.csv`, variant `updated`).

Sizes: `size_mb` is the uncompressed image (sum of layer sizes, what lands on disk); `compressed_mb` is
the registry transfer size; `java_home_mb` is the installed Java directory alone. Upgrading always adds a
layer on top of the original files, so an updated image is never smaller than its base.

Vulnerabilities: trivy findings over OS packages and bundled Java libraries, all severities, fixed and
unfixed, counted per occurrence as trivy does; the `fixable_*` columns are the subset with a fix
available. Counts include binaries trivy can analyse inside the base image: Ubuntu 26.04 ships a Go binary
(`pebble`) whose findings no apt upgrade removes. Every image is also probed for its Java runtime version
and vendor string.

`recommendations.csv` picks, per Java version and flavor, the image with no critical or high findings,
then fewest medium and low, then smallest, and lists the best non-Alpine candidate separately for
workloads that need glibc.

## libc

Alpine is musl, everything else is glibc; no surveyed image uses uClibc. Vendors ship separate musl
builds of the JDK for Alpine, so those are native musl binaries. Known consequences for Java workloads:

- **JNI libraries in dependencies**: a Java library that bundles a native `.so` must bundle a musl build
  too. Verified with a Spring Boot application on the surveyed images: zstd-jni, lz4-java and JNA work
  on both; snappy-java's Linux library is glibc-linked and fails on Alpine unless the `gcompat` package
  is installed (about 300 KB). Kafka consumers meet snappy whenever a producer used it.
- **Native library extraction**: snappy-java and zstd-jni extract their `.so` into `java.io.tmpdir` and
  load it from there, so `/tmp` must be executable. Docker's `--tmpfs /tmp` is noexec by default and
  breaks both on glibc and musl alike; Kubernetes emptyDir is executable.
- **A glibc JVM on Alpine is not an option.** Alpine's `gcompat` shim cannot start a glibc-built JVM,
  and on the community `frolvlad/alpine-glibc` image the Corretto and Zulu 21 JVMs segfault at
  startup; no vendor supports that layout. Use a glibc OS for glibc workloads.
- **Memory**: musl's allocator fragments more than glibc's under many threads, so container limits need
  somewhat more headroom for native memory on Alpine, or jemalloc.
- **Package tooling**: Alpine images carry busybox, `apk`, `adduser` and `wget`; there is no bash, curl
  or `useradd` unless installed. Dockerfiles written for a dnf-based image do not transfer unchanged.

## Running

Requires docker with BuildKit, trivy and python3. Docker Hub pulls should be authenticated
(`docker login`); the anonymous rate limit stalls the pull stage, which then waits and retries.

```
python3 jbi.py all -j 6                        # full run into results/<today>/
python3 jbi.py all --vendor temurin --java 25  # filters: --vendor --java --os --flavor --variant --method
python3 jbi.py build measure scan report --retry-failed
JBI_DOCKER="sudo -g docker docker" JBI_TRIVY="sudo -g docker trivy" python3 jbi.py all   # socket via group
```

Stages: `pull` (base images, deduplicated), `generate` (Dockerfiles into `dockerfiles/`, apt keys into
`build/keys/`), `build` (`--no-cache`), `measure`, `scan` (one trivy cache per worker), `report`,
`recommend`, `baseos` (the plain OS bases). Nothing is pinned by digest on purpose: every run measures
the current state of the tags. Base image digests, trivy version and DB timestamp are recorded.

## Results

`results/<run-id>/`: `summary.csv` and `report.md` (Java images, one row per cell and variant,
including not-available cells), `base-os.csv` and `base-os.md`, `recommendations.csv` and
`recommendations.md`, `images/*.json` (raw per-image measurements). `trivy/` and `logs/` are not
committed. Vendor support and image update policies are collected in
[docs/support-policies.md](docs/support-policies.md). Licensed under the MIT license, see [LICENSE](LICENSE).
