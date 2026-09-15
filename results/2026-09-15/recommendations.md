# Recommended images -- run 2026-09-15

Rule: no critical or high findings; then fewest medium+low findings; then smallest uncompressed size. `glibc` rows are the best candidate outside Alpine (musl) for workloads that need glibc. Rank 2+ rows are the runners-up under the same rule.

| Java | Flavor | Kind | Vendor | OS | Variant | Method | Size MB | Compressed MB | OS version | Java version | Medium | Low | Caveat |
|---|---|---|---|---|---|---|---:|---:|---|---|---:|---:|---|
| 17 | jdk | recommended | zulu | alpine | updated | official | 303.7 | 153.9 | Alpine Linux v3.23 | 17.0.20.1+1-LTS | 0 | 0 | Azul pins Alpine 3.23 in the Docker Official Image; community builds have no published end-of-updates dates |
| 17 | jdk | glibc | microsoft | azurelinux | base | official | 466.7 | 212.3 | Microsoft Azure Linux 3.0 | 17.0.20.1+1-LTS | 0 | 0 |  |
| 17 | jre | recommended | temurin | alpine | updated | official | 199.4 | 71.5 | Alpine Linux v3.24 | 17.0.20+8 | 0 | 0 | official image lags the quarterly release by 2-5 weeks |
| 17 | jre | glibc | corretto | al2023 | updated | official | 413.2 | 143.2 | Amazon Linux 2023.12.20260914 | 17.0.20.1+10-LTS | 0 | 0 | published image is a repository snapshot; upgrade with --releasever=latest |
| 21 | jdk | recommended | zulu | alpine | updated | official | 330.5 | 166.9 | Alpine Linux v3.23 | 21.0.12.1+1-LTS | 0 | 0 | Azul pins Alpine 3.23 in the Docker Official Image; community builds have no published end-of-updates dates |
| 21 | jdk | glibc | redhat | ubi10-minimal | base | official | 378.5 | 141.7 | Red Hat Enterprise Linux 10.2 (Coughlan) | 21.0.12.1+1-LTS | 0 | 0 |  |
| 21 | jre | recommended | temurin | alpine | updated | official | 223.1 | 77.5 | Alpine Linux v3.24 | 21.0.12+8-LTS | 0 | 0 | official image lags the quarterly release by 2-5 weeks |
| 21 | jre | glibc | redhat | ubi10-minimal | base | official | 338.7 | 118.1 | Red Hat Enterprise Linux 10.2 (Coughlan) | 21.0.12.1+1-LTS | 0 | 0 |  |
| 25 | jdk | recommended | temurin | alpine | updated | official | 319.0 | 113.3 | Alpine Linux v3.24 | 25.0.4+7-LTS | 0 | 0 | official image lags the quarterly release by 2-5 weeks |
| 25 | jdk | glibc | redhat | ubi10-minimal | base | official | 420.2 | 156.9 | Red Hat Enterprise Linux 10.2 (Coughlan) | 25.0.4.1+1-LTS | 0 | 0 |  |
| 25 | jre | recommended | temurin | alpine | updated | official | 240.7 | 78.9 | Alpine Linux v3.24 | 25.0.4+7-LTS | 0 | 0 | official image lags the quarterly release by 2-5 weeks |
| 25 | jre | glibc | redhat | ubi10-minimal | base | official | 380.2 | 133.2 | Red Hat Enterprise Linux 10.2 (Coughlan) | 25.0.4.1+1-LTS | 0 | 0 |  |

## Runners-up

| Java | Flavor | Rank | Vendor | OS | Variant | Size MB | Medium | Low | Java version |
|---|---|---|---|---|---|---:|---:|---:|---|
| 17 | jdk | 2 | corretto | alpine | updated | 308.0 | 0 | 0 | 17.0.20.1+10-LTS |
| 17 | jdk | 3 | temurin | alpine | updated | 352.3 | 0 | 0 | 17.0.20+8 |
| 17 | jdk | 4 | microsoft | azurelinux | base | 466.7 | 0 | 0 | 17.0.20.1+1-LTS |
| 17 | jdk | 5 | microsoft | azurelinux | updated | 466.8 | 0 | 0 | 17.0.20.1+1-LTS |
| 17 | jre | 2 | zulu | alpine | updated | 213.9 | 0 | 0 | 17.0.20.1+1-LTS |
| 17 | jre | 3 | corretto | al2023 | updated | 413.2 | 0 | 0 | 17.0.20.1+10-LTS |
| 21 | jdk | 2 | corretto | alpine | updated | 335.2 | 0 | 0 | 21.0.12.1+9-LTS |
| 21 | jdk | 3 | redhat | ubi10-minimal | base | 378.5 | 0 | 0 | 21.0.12.1+1-LTS |
| 21 | jdk | 4 | temurin | alpine | updated | 379.8 | 0 | 0 | 21.0.12+8-LTS |
| 21 | jdk | 5 | redhat | ubi10-minimal | updated | 405.5 | 0 | 0 | 21.0.12.1+1-LTS |
| 21 | jre | 2 | zulu | alpine | updated | 231.7 | 0 | 0 | 21.0.12.1+1-LTS |
| 21 | jre | 3 | redhat | ubi10-minimal | base | 338.7 | 0 | 0 | 21.0.12.1+1-LTS |
| 21 | jre | 4 | redhat | ubi10-minimal | updated | 363.5 | 0 | 0 | 21.0.12.1+1-LTS |
| 21 | jre | 5 | corretto | al2023 | updated | 433.8 | 0 | 0 | 21.0.12.1+9-LTS |
| 25 | jdk | 2 | zulu | alpine | updated | 376.9 | 0 | 0 | 25.0.4.1+1-LTS |
| 25 | jdk | 3 | corretto | alpine | updated | 381.1 | 0 | 0 | 25.0.4.1+8-LTS |
| 25 | jdk | 4 | redhat | ubi10-minimal | base | 420.2 | 0 | 0 | 25.0.4.1+1-LTS |
| 25 | jdk | 5 | redhat | ubi10-minimal | updated | 449.2 | 0 | 0 | 25.0.4.1+1-LTS |
| 25 | jre | 2 | zulu | alpine | updated | 273.0 | 0 | 0 | 25.0.4.1+1-LTS |
| 25 | jre | 3 | redhat | ubi10-minimal | base | 380.2 | 0 | 0 | 25.0.4.1+1-LTS |
| 25 | jre | 4 | redhat | ubi10-minimal | updated | 405.0 | 0 | 0 | 25.0.4.1+1-LTS |
| 25 | jre | 5 | corretto | al2023 | updated | 474.9 | 0 | 0 | 25.0.4.1+8-LTS |
