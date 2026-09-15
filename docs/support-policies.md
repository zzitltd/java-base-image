# Vendor support policies for the surveyed Java images

Verified against vendor pages on 2026-09-15. Every fact carries its source URL; items that could not be
confirmed from a vendor page are listed at the end. Dates are the vendors' own wording ("at least",
"planned") and move over time. Scope follows the survey: Java 17, 21 and 25, JDK and JRE, on the OS
bases listed in the README.

## 1. End of free updates, by vendor and Java version

Free means updates published without a paid contract. Paid tiers are noted where they extend the date.

| Java | Oracle OpenJDK (GPL image) | Red Hat (RHEL/UBI) | Microsoft | Corretto | Temurin | Zulu (community) |
|---|---|---|---|---|---|---|
| 17 | 17.0.2, Jan 2022, frozen | 2027-12-31 (ELS to 2029-01) | Sep 2027 | Jul 2029 (EOL Oct 2029) | at least Oct 2027 | not published (Core: Sep 2029) |
| 21 | 21.0.2, Jan 2024, frozen | 2029-12-31 (ELS to 2031-09) | Sep 2028 | Jul 2030 (EOL Oct 2030) | at least Dec 2029 | not published (Core: Sep 2031) |
| 25 | 25.0.2, Jan 2026, frozen | 2030-12-31 (ELS to 2033-09) | Sep 2030 | Jul 2032 (EOL Oct 2032) | at least Sep 2031 | not published (Core: Sep 2033) |

All vendors except Oracle OpenJDK ship on the OpenJDK quarterly cycle (third Tuesday of January, April,
July, October). Oracle's GPL OpenJDK builds stop at the next feature release, six months after GA.

## 2. Oracle

**Distribution.** Oracle OpenJDK (GPLv2+CPE) is built only for the current feature release; the JDK FAQ
lists the last free OpenJDK update per LTS line: 17.0.2, 21.0.2, 25.0.2 (https://www.oracle.com/java/technologies/javase/jdk-faqs.html).
jdk.java.net marks 21 and 25 as "superseded" and the archive warns those builds "are not updated with the
latest security patches and are not recommended for use in production" (https://jdk.java.net/archive/).
Oracle JDK (the licensed build) is a different product: NFTC allows free production use of 21 until
September 2026 and 25 until September 2028, after which updates move to the OTN license; Premier support
ends September 2028 (21) and September 2030 (25) (https://www.oracle.com/java/technologies/java-se-support-roadmap.html).
"Oracle does not offer support for OpenJDK" (https://container-registry.oracle.com/ords/ocr/ba/java/openjdk).

**Images.** `container-registry.oracle.com/java/openjdk`: only the current line is rebuilt; older tags
stay pullable but frozen at the last OpenJDK update (17.0.2 on Oracle Linux 8, 21.0.2 on Oracle Linux 8,
25.0.2 on Oracle Linux 9). Licensed images live in `java/jdk` (login and terms acceptance) and
`java/jdk-no-fee-term` (anonymous, NFTC; 21 updated until September 2026, 25 until September 2028).
Base OS rule for the licensed images: the Oracle Linux version recommended at the JDK's initial release,
kept for as long as that version is in Premier support (https://container-registry.oracle.com/ords/ocr/ba/java/jdk).
Oracle recommends `yum -y update` in downstream Dockerfiles. No JRE images.

**Reading the rows.** The Oracle rows show what a pull of the tag gives today. None of them is a
supportable base past the next feature release.

## 3. Red Hat

**Distribution.** "OpenJDK Life Cycle and Support Policy" (https://access.redhat.com/articles/1299013):
six years of support per version, four updates per year. Full support ends 2027-12-31 (17), 2029-12-31
(21), 2030-12-31 (25); ELS-1 is a separate paid subscription. RHEL 10 carries only OpenJDK 21 and 25.
Entitlement for Java workloads is part of a RHEL subscription; the lifecycle dates apply to the container
images as well.

**Images.** Source: https://github.com/rh-openjdk/redhat-openjdk-containers. All are built on
`ubi-minimal` with microdnf. Builder images (`ubi9/openjdk-17|21|25`, `ubi10/openjdk-21|25`) contain
`java-N-openjdk-devel`, Maven 3.9 and S2I scripts, which is why they are larger than a plain UBI plus
JDK. Runtime images (`-runtime`) contain `java-N-openjdk-headless` only. All of these were GA and
rebuilt on 2026-09-14/15 in the Red Hat Ecosystem Catalog. There is no `ubi10/openjdk-17` because RHEL
10 does not ship OpenJDK 17.

**Rebuild policy.** UBI images are rebuilt "on a 6 weekly cadence, or sooner if triggered by the release
of a CVE rated as Critical or Important"; updates only for the most current image (https://access.redhat.com/support/policy/updates/ubi).
Base RHEL/UBI images are rebuilt whenever a contained RPM is updated (https://access.redhat.com/articles/2208321).
The Container Health Index grades images A to F by age of unapplied Critical/Important errata (https://access.redhat.com/articles/2803031).

**Support scope.** Container support requires a supported Red Hat platform and subscription; the policy
covers every UBI variant identically (https://access.redhat.com/articles/2726611). UBI is freely
redistributable under the UBI EULA, which grants no maintenance or support rights and forbids implying
Red Hat support for derived images (https://www.redhat.com/licenses/EULA_Red_Hat_Universal_Base_Image_English_20190422.pdf).
Without a subscription only the UBI BaseOS and AppStream repos are reachable; they contain the OpenJDK
packages (https://access.redhat.com/articles/4238681). Findings in UBI 9 packages that Red Hat has not
fixed in the UBI repos stay in the image regardless of upgrading.

**Reading the rows.** The `ubi9` and `ubi10` standard rows are self-built and get the same packages as
the official images, minus Maven and S2I.

## 4. Microsoft

**Distribution.** Support policy (https://learn.microsoft.com/en-us/java/openjdk/support): LTS releases
only, quarterly updates in January, April, July, October, free for anyone. Earliest end of support:
September 2027 (17), September 2028 (21), September 2030 (25); "initial targets", may be extended.
Commercial support is only for Azure customers with an Azure Support Plan and only for workloads on Azure,
Azure Stack or Azure Arc; everyone else gets community support on GitHub.

**Images.** `mcr.microsoft.com/openjdk/jdk` (https://learn.microsoft.com/en-us/java/openjdk/containers):
Azure Linux 3.0, Ubuntu 22.04 and Azure Linux distroless variants; amd64 and arm64. Images are "rebuilt
every Monday, Wednesday, and Friday". No minor-version tags: the major tag always carries the latest
update. No JRE images; Microsoft documents jlink instead. A non-root `app` user is provided.

**Azure Linux.** Support and lifecycle commitments "apply only to Azure scenarios"; container images are
in scope, bare metal and other clouds are not (https://learn.microsoft.com/en-us/azure/azure-linux/support-options).
Azure Linux 3.0 GA August 2024; "each major version for 3 years", EOL "Summer 2027" per a Microsoft
Tech Community post, not a lifecycle page (https://techcommunity.microsoft.com/blog/azurearcblog/eol-of-azure-linux-2-0-on-azure-kubernetes-service-enabled-by-azure-arc/4434242).

## 5. Amazon Corretto

**Distribution.** FAQ support calendar (https://aws.amazon.com/corretto/faqs/): Last Planned Update and
End of Life: 17 Jul 2029 / Oct 2029; 21 Jul 2030 / Oct 2030; 25 Jul 2032 / Oct 2032. Quarterly updates
plus out-of-cycle urgent fixes. Free for everyone; covered by an existing AWS Support Plan like any AWS
software, no Corretto-specific plan; others use GitHub issues.

**Images.** Docker Hub `amazoncorretto` and ECR Public, Dockerfiles at https://github.com/corretto/corretto-docker.
Variants: Amazon Linux 2023 (default), Amazon Linux 2 (end of life, "provided only as a fallback"),
Alpine 3.21 to 3.24; Debian Dockerfiles are examples only, no prebuilt images. JRE variants exist as
`headless` and `headful` on Amazon Linux 2023 only; Alpine, Debian and Ubuntu get JDK packages only.

**Rebuild policy.** "It is the responsibility of the base docker image supplier to provide timely
security updates ... The amazoncorretto images are automatically rebuilt when a new base image is made
available, but we do not make changes to our Dockerfiles to pull in one-off package updates." Users are
told to run `dnf update -y --security --releasever=latest` or `apk -U upgrade` themselves. Major-version
tags always point at the latest security update; superseded tags remain but stop receiving base updates.
Containers run as root (no `USER` in the Dockerfiles).

**Amazon Linux 2023.** Standard support to 2027-06-30, maintenance to 2029-06-30, quarterly minor
releases; images lock to a repository snapshot, so `dnf upgrade` without `--releasever=latest` stays on
the image's snapshot (https://docs.aws.amazon.com/linux/al2023/ug/release-cadence.html).

## 6. Eclipse Temurin

**Distribution.** "We will support LTS releases for at least four years"; builds continue "as long as the
corresponding upstream source is actively maintained". End of availability: at least Oct 2027 (17),
Dec 2029 (21), Sep 2031 (25) (https://adoptium.net/support/). Support is community, best effort;
commercial support is via third parties listed but not endorsed by Adoptium: IBM, ManageCat, Open
Elements, Red Hat (https://adoptium.net/temurin/commercial-support).

**Images.** `eclipse-temurin` is a Docker Official Image built and published by Docker Inc from
Adoptium's Dockerfiles (https://github.com/adoptium/containers). Base OS config (config/temurin.yml):
Ubuntu 26.04 (`resolute`, the default), 24.04 and 22.04; UBI 10 minimal; UBI 9 minimal for Java 21 and
older; Alpine 3.24 and 3.23; Windows. JRE images exist for every version, though jlink is recommended
from 21 on. Alpine tags carry the minor version (`21-jdk-alpine-3.24`); the unsuffixed `-alpine` tag
moves to the newest Alpine. A distribution may be dropped mid Java LTS if it reaches upstream end of life
(https://github.com/adoptium/containers/blob/main/DISTRO_MAINTENANCE.md). No Debian images; Debian
gets the Adoptium apt repo.

**Rebuild policy.** Docker rebuilds base-OS layers "in short order" for critical CVEs; Ubuntu images are
rebuilt "about once a month"; Adoptium cannot trigger a rebuild other than by changing a Dockerfile. JDK
updates arrive by Dockerfile PRs from an updater that runs every 30 minutes, but the Docker Hub manifest
waits until all binaries for all platforms are published. Observed lag from quarterly release to image:
two to five weeks in 2026. SBOMs are published for the JDK binaries, not for the images. Containers run
as root.

**Reading the rows.** Official Temurin images can carry an older point release than the apt repo on
the same day; that is the documented manifest lag, not a packaging error.

## 7. Azul Zulu

**Distribution.** Two tiers: Zulu community builds are free, provided "AS IS", with no support obligation
and no published end-of-updates dates (https://www.azul.com/products/core/openjdk-terms-of-use/).
Azul Platform Core is paid: quarterly CPUs, monthly Critical Security Patch Updates, SLA on delivery
("max 48 hours, target same day as Oracle" on the Premium tier), 8 years production plus 2 years extended
support (https://www.azul.com/products/core/). Roadmap production support ends Sep 2029 (17), Sep 2031
(21), Sep 2033 (25) (https://www.azul.com/products/azul-support-roadmap/). In practice community builds
have shipped every quarter to date; the July 2026 builds were released on 2026-07-21, Oracle's CPU day,
for both tiers (https://docs.azul.com/core/release/july-2026/release-notes). Security-only CPU builds are
paid only; community gets the PSU builds.

**Images.** The survey uses the Docker Official Image `azul-zulu` (https://hub.docker.com/_/azul-zulu,
source https://github.com/AzulSystems/azul-zulu-images): Java 8 to 26; `jdk`, `jdk-headless`, `jre`,
`jre-headless`; Debian 13 (default), Alpine 3.23, AlmaLinux 10; amd64 and arm64; the Zulu package is
pinned and no OS upgrade runs at build; rebuilt automatically when the base image changes, per Docker's
Official Images process. The older `azul/zulu-openjdk*` repositories (Ubuntu, Debian 12, Alpine 3.20,
CentOS 7) "will be retired by the end of 2026" (https://github.com/zulu-openjdk/zulu-openjdk) and are
not used. No Ubuntu variant exists in the new image; Ubuntu gets Azul's apt repo
(`repos.azul.com/zulu/deb`).

## 8. OS base lifecycles

| OS | Release | End of support | Source |
|---|---|---|---|
| Alpine 3.24 | 2026-06-09 | 2028-06-01 (main repo 2 years) | https://alpinelinux.org/releases/ |
| Alpine 3.23 (Zulu's pin) | 2025-12-03 | 2027-11-01 | same |
| Debian 13 trixie | 2025-08-09 | full support about 3 years, then LTS to 2030-06-30 | https://www.debian.org/releases/, https://wiki.debian.org/LTS |
| Ubuntu 26.04 LTS | 2026-04 | standard support 5 years, to 2031-04; ESM beyond | https://ubuntu.com/about/release-cycle |
| RHEL 9 / UBI 9 | 2022-05-18 | full 2027-05-31, maintenance 2032-05-31 | https://access.redhat.com/product-life-cycles/?product=Red%20Hat%20Enterprise%20Linux |
| RHEL 10 / UBI 10 | 2025-05-20 | full 2030-05-31, maintenance 2035-05-31 | same |
| Amazon Linux 2023 | 2023-03 | standard 2027-06-30, maintenance 2029-06-30 | https://docs.aws.amazon.com/linux/al2023/ug/release-cadence.html |
| Oracle Linux 8 | 2019-07 | premier 2029-07, extended 2032-07 | https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf |
| Oracle Linux 9 | 2022-06 | premier 2032-06, extended 2035-06 | same |
| Azure Linux 3.0 | 2024-08 | "Summer 2027" (3 years) | Tech Community post cited in section 4 |

UBI has no EUS phase and updates only the current image; content availability follows the RHEL release
lifecycle (https://access.redhat.com/support/policy/updates/ubi). Debian and Ubuntu Official Images are
rebuilt at least monthly and sooner for critical security issues, and every Official Image built FROM
them is rebuilt with them (https://github.com/docker-library/faq).

## 9. Cross-cutting observations

- Only Red Hat, Microsoft and Oracle (paid JDK) offer a contract-backed support statement for the image
  itself; Corretto is covered by AWS Support plans, Temurin and Zulu community builds are community only.
- Corretto, Temurin and Zulu make OS package updates the user's job between base-image rebuilds.
  Microsoft rebuilds three times a week, Red Hat within days for Critical/Important CVEs or at least
  every six weeks.
- Oracle's GPL OpenJDK 17, 21 and 25 images are frozen streams.
- A vendor's end of updates is not the same as the OS base's end of life; the earlier of the two applies.
  Alpine's two-year window is the shortest in the table, Amazon Linux 2023 the next (mid-2029).

## 10. Not verified from a vendor page

- Oracle: the canonical blog post on the six-month OpenJDK policy returned 403; the policy is evidenced
  by the JDK FAQ table, jdk.java.net "superseded" pages and the frozen registry tags.
- Red Hat: no per-image EOL dates for GA streams; the RHEL date table on the errata page is JS-rendered,
  so dates come from the Product Life Cycles API.
- Microsoft: Azure Linux 3.0 EOL appears only in a Tech Community post; learn.microsoft.com publishes no
  date. Rebuild on PSU day specifically is not stated, only the Monday/Wednesday/Friday cadence.
- Corretto: root user is observed from the Dockerfiles, not stated. No vendor statement on tag deletion.
- Temurin: the image rebuild cadence beyond "about once a month" and "in short order" is not documented;
  the two-to-five-week lag is observed from Docker Hub manifest commits.
- Zulu: no end-of-updates dates for the free builds; no written rebuild policy beyond the Docker
  Official Images process.
- Ubuntu 26.04: dates follow Ubuntu's standard LTS policy; the release-specific page was not fetched.
