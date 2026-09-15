# Java image matrix -- run 2026-09-15

Generated 2026-09-15 20:41 UTC with trivy 0.73.0, DB 2026-09-15T07:08:16.463168542Z. Vulnerability columns count trivy findings over OS packages and bundled Java libraries, all severities, fixed and unfixed; the number in parentheses is the fixable subset. Size is the uncompressed image on disk, compressed is the registry transfer size. `base` is the vendor image as published, `updated` has the OS packages upgraded (for repo installs the OS is upgraded before Java is installed).

| Vendor | Java | OS | Flavor | Variant | Method | Size MB | Compressed MB | Java home MB | OS version | libc | Java version | Critical | High | Medium | Low |
|---|---|---|---|---|---|---:|---:|---:|---|---|---|---:|---:|---:|---:|
| oracle | 17 | oraclelinux | jdk | base | official | 600.7 | 281.4 | 322.7 | Oracle Linux Server 8.5 | glibc 2.28 | 17.0.2+8-86 | 0 (0) | 203 (203) | 307 (307) | 21 (21) |
| oracle | 17 | oraclelinux | jdk | updated | official | 1006.0 | 425.9 | 322.7 | Oracle Linux Server 8.10 | glibc 2.28 | 17.0.2+8-86 | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| oracle | 21 | oraclelinux | jdk | base | official | 713.2 | 330.0 | 353.9 | Oracle Linux Server 8.9 | glibc 2.28 | 21.0.2+13-58 | 0 (0) | 158 (158) | 178 (178) | 7 (7) |
| oracle | 21 | oraclelinux | jdk | updated | official | 1041.0 | 449.9 | 353.9 | Oracle Linux Server 8.10 | glibc 2.28 | 21.0.2+13-58 | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| oracle | 25 | oraclelinux | jdk | base | official | 689.5 | 329.6 | 400.0 | Oracle Linux Server 9.7 | glibc 2.34 | 25.0.2+10-69 | 0 (0) | 148 (148) | 146 (146) | 3 (3) |
| oracle | 25 | oraclelinux | jdk | updated | official | 951.4 | 428.3 | 400.0 | Oracle Linux Server 9.8 | glibc 2.34 | 25.0.2+10-69 | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| redhat | 17 | ubi9-minimal | jdk | base | official | 429.2 | 153.5 | 216.4 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 17.0.20.1+1-LTS | 0 (0) | 10 (0) | 178 (1) | 91 (0) |
| redhat | 17 | ubi9-minimal | jdk | updated | official | 453.7 | 160.8 | 216.4 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 17.0.20.1+1-LTS | 0 (0) | 10 (0) | 177 (0) | 91 (0) |
| redhat | 17 | ubi9-minimal | jre | base | official | 392.8 | 132.1 | 205.9 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 17.0.20.1+1-LTS | 0 (0) | 7 (0) | 125 (1) | 85 (0) |
| redhat | 17 | ubi9-minimal | jre | updated | official | 415.3 | 138.6 | 205.9 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 17.0.20.1+1-LTS | 0 (0) | 7 (0) | 124 (0) | 85 (0) |
| redhat | 17 | ubi9 | jdk | updated | repo | 493.5 | 167.8 | 216.4 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 17.0.20.1+1-LTS | 0 (0) | 13 (0) | 180 (0) | 251 (0) |
| redhat | 17 | ubi9 | jre | updated | repo | 471.0 | 157.0 | 205.9 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 17.0.20.1+1-LTS | 0 (0) | 10 (0) | 164 (0) | 249 (0) |
| redhat | 21 | ubi9-minimal | jdk | base | official | 448.2 | 162.0 | 235.4 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 21.0.12.1+1-LTS | 0 (0) | 10 (0) | 178 (1) | 91 (0) |
| redhat | 21 | ubi9-minimal | jdk | updated | official | 472.8 | 169.3 | 235.4 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 21.0.12.1+1-LTS | 0 (0) | 10 (0) | 177 (0) | 91 (0) |
| redhat | 21 | ubi9-minimal | jre | base | official | 409.7 | 139.1 | 222.8 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 21.0.12.1+1-LTS | 0 (0) | 7 (0) | 125 (1) | 85 (0) |
| redhat | 21 | ubi9-minimal | jre | updated | official | 432.2 | 145.6 | 222.8 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 21.0.12.1+1-LTS | 0 (0) | 7 (0) | 124 (0) | 85 (0) |
| redhat | 21 | ubi9 | jdk | updated | repo | 512.5 | 176.3 | 235.4 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 21.0.12.1+1-LTS | 0 (0) | 13 (0) | 180 (0) | 251 (0) |
| redhat | 21 | ubi9 | jre | updated | repo | 488.0 | 163.9 | 222.8 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 21.0.12.1+1-LTS | 0 (0) | 10 (0) | 164 (0) | 249 (0) |
| redhat | 21 | ubi10-minimal | jdk | base | official | 378.5 | 141.7 | 235.4 | Red Hat Enterprise Linux 10.2 (Coughlan) | glibc 2.39 | 21.0.12.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| redhat | 21 | ubi10-minimal | jdk | updated | official | 405.5 | 150.7 | 235.4 | Red Hat Enterprise Linux 10.2 (Coughlan) | glibc 2.39 | 21.0.12.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| redhat | 21 | ubi10-minimal | jre | base | official | 338.7 | 118.1 | 222.7 | Red Hat Enterprise Linux 10.2 (Coughlan) | glibc 2.39 | 21.0.12.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| redhat | 21 | ubi10-minimal | jre | updated | official | 363.5 | 126.2 | 222.7 | Red Hat Enterprise Linux 10.2 (Coughlan) | glibc 2.39 | 21.0.12.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| redhat | 21 | ubi10 | jdk | updated | repo | 512.1 | 177.6 | 235.4 | Red Hat Enterprise Linux 10.2 (Coughlan) | glibc 2.39 | 21.0.12.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| redhat | 21 | ubi10 | jre | updated | repo | 486.3 | 164.8 | 222.7 | Red Hat Enterprise Linux 10.2 (Coughlan) | glibc 2.39 | 21.0.12.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| redhat | 25 | ubi9-minimal | jdk | base | official | 490.1 | 177.2 | 276.9 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 25.0.4.1+1-LTS | 0 (0) | 15 (0) | 183 (1) | 92 (0) |
| redhat | 25 | ubi9-minimal | jdk | updated | official | 514.7 | 184.5 | 276.9 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 25.0.4.1+1-LTS | 0 (0) | 15 (0) | 182 (0) | 92 (0) |
| redhat | 25 | ubi9-minimal | jre | base | official | 450.2 | 153.8 | 264.1 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 25.0.4.1+1-LTS | 0 (0) | 10 (0) | 130 (1) | 86 (0) |
| redhat | 25 | ubi9-minimal | jre | updated | official | 472.6 | 160.3 | 264.1 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 25.0.4.1+1-LTS | 0 (0) | 10 (0) | 129 (0) | 86 (0) |
| redhat | 25 | ubi9 | jdk | updated | repo | 553.2 | 190.9 | 276.9 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 25.0.4.1+1-LTS | 0 (0) | 18 (0) | 185 (0) | 252 (0) |
| redhat | 25 | ubi9 | jre | updated | repo | 528.5 | 178.5 | 264.1 | Red Hat Enterprise Linux 9.8 (Plow) | glibc 2.34 | 25.0.4.1+1-LTS | 0 (0) | 13 (0) | 169 (0) | 250 (0) |
| redhat | 25 | ubi10-minimal | jdk | base | official | 420.2 | 156.9 | 276.9 | Red Hat Enterprise Linux 10.2 (Coughlan) | glibc 2.39 | 25.0.4.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| redhat | 25 | ubi10-minimal | jdk | updated | official | 449.2 | 166.7 | 276.9 | Red Hat Enterprise Linux 10.2 (Coughlan) | glibc 2.39 | 25.0.4.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| redhat | 25 | ubi10-minimal | jre | base | official | 380.2 | 133.2 | 264.1 | Red Hat Enterprise Linux 10.2 (Coughlan) | glibc 2.39 | 25.0.4.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| redhat | 25 | ubi10-minimal | jre | updated | official | 405.0 | 141.2 | 264.1 | Red Hat Enterprise Linux 10.2 (Coughlan) | glibc 2.39 | 25.0.4.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| redhat | 25 | ubi10 | jdk | updated | repo | 553.8 | 192.5 | 276.9 | Red Hat Enterprise Linux 10.2 (Coughlan) | glibc 2.39 | 25.0.4.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| redhat | 25 | ubi10 | jre | updated | repo | 527.8 | 179.6 | 264.1 | Red Hat Enterprise Linux 10.2 (Coughlan) | glibc 2.39 | 25.0.4.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| microsoft | 17 | azurelinux | jdk | base | official | 466.7 | 212.3 | 281.2 | Microsoft Azure Linux 3.0 | glibc 2.38 | 17.0.20.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| microsoft | 17 | azurelinux | jdk | updated | official | 466.8 | 212.3 | 281.2 | Microsoft Azure Linux 3.0 | glibc 2.38 | 17.0.20.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| microsoft | 21 | azurelinux | jdk | base | official | 494.1 | 225.5 | 308.5 | Microsoft Azure Linux 3.0 | glibc 2.38 | 21.0.12.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| microsoft | 21 | azurelinux | jdk | updated | official | 494.1 | 225.5 | 308.5 | Microsoft Azure Linux 3.0 | glibc 2.38 | 21.0.12.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| microsoft | 25 | azurelinux | jdk | base | official | 538.7 | 244.2 | 353.1 | Microsoft Azure Linux 3.0 | glibc 2.38 | 25.0.4.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| microsoft | 25 | azurelinux | jdk | updated | official | 538.7 | 244.2 | 353.1 | Microsoft Azure Linux 3.0 | glibc 2.38 | 25.0.4.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| corretto | 17 | alpine | jdk | base | official | 301.4 | 152.8 | 285.1 | Alpine Linux v3.24 | musl 1.2.6 | 17.0.20.1+10-LTS | 0 (0) | 2 (2) | 6 (6) | 12 (12) |
| corretto | 17 | alpine | jdk | updated | official | 308.0 | 155.6 | 285.1 | Alpine Linux v3.24 | musl 1.2.6 | 17.0.20.1+10-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| corretto | 17 | debian | jdk | updated | repo | 471.3 | 244.9 | 336.5 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 17.0.20.1+10-LTS | 0 (0) | 43 (0) | 47 (0) | 56 (0) |
| corretto | 17 | ubuntu | jdk | updated | repo | 483.0 | 251.9 | 336.5 | Ubuntu 26.04.1 LTS | glibc 2.43 | 17.0.20.1+10-LTS | 0 (0) | 8 (8) | 26 (0) | 4 (0) |
| corretto | 17 | al2023 | jdk | base | official | 478.8 | 211.7 | 277.0 | Amazon Linux 2023.12.20260831 | glibc 2.34 | 17.0.20.1+10-LTS | 0 (0) | 29 (29) | 30 (30) | 0 (0) |
| corretto | 17 | al2023 | jdk | updated | official | 497.1 | 217.9 | 277.0 | Amazon Linux 2023.12.20260914 | glibc 2.34 | 17.0.20.1+10-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| corretto | 17 | al2023 | jre | base | official | 395.5 | 137.1 | 195.9 | Amazon Linux 2023.12.20260831 | glibc 2.34 | 17.0.20.1+10-LTS | 0 (0) | 29 (29) | 30 (30) | 0 (0) |
| corretto | 17 | al2023 | jre | updated | official | 413.2 | 143.2 | 195.9 | Amazon Linux 2023.12.20260914 | glibc 2.34 | 17.0.20.1+10-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| corretto | 21 | alpine | jdk | base | official | 328.6 | 166.1 | 312.3 | Alpine Linux v3.24 | musl 1.2.6 | 21.0.12.1+9-LTS | 0 (0) | 2 (2) | 6 (6) | 12 (12) |
| corretto | 21 | alpine | jdk | updated | official | 335.2 | 168.8 | 312.3 | Alpine Linux v3.24 | musl 1.2.6 | 21.0.12.1+9-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| corretto | 21 | debian | jdk | updated | repo | 499.8 | 260.3 | 365.0 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 21.0.12.1+9-LTS | 0 (0) | 43 (0) | 47 (0) | 56 (0) |
| corretto | 21 | ubuntu | jdk | updated | repo | 511.5 | 267.2 | 365.0 | Ubuntu 26.04.1 LTS | glibc 2.43 | 21.0.12.1+9-LTS | 0 (0) | 8 (8) | 26 (0) | 4 (0) |
| corretto | 21 | al2023 | jdk | base | official | 506.1 | 225.0 | 304.3 | Amazon Linux 2023.12.20260831 | glibc 2.34 | 21.0.12.1+9-LTS | 0 (0) | 29 (29) | 30 (30) | 0 (0) |
| corretto | 21 | al2023 | jdk | updated | official | 524.4 | 231.2 | 304.3 | Amazon Linux 2023.12.20260914 | glibc 2.34 | 21.0.12.1+9-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| corretto | 21 | al2023 | jre | base | official | 416.1 | 143.9 | 216.4 | Amazon Linux 2023.12.20260831 | glibc 2.34 | 21.0.12.1+9-LTS | 0 (0) | 29 (29) | 30 (30) | 0 (0) |
| corretto | 21 | al2023 | jre | updated | official | 433.8 | 150.0 | 216.4 | Amazon Linux 2023.12.20260914 | glibc 2.34 | 21.0.12.1+9-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| corretto | 25 | alpine | jdk | base | official | 374.6 | 185.4 | 358.3 | Alpine Linux v3.24 | musl 1.2.6 | 25.0.4.1+8-LTS | 0 (0) | 2 (2) | 6 (6) | 12 (12) |
| corretto | 25 | alpine | jdk | updated | official | 381.1 | 188.1 | 358.3 | Alpine Linux v3.24 | musl 1.2.6 | 25.0.4.1+8-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| corretto | 25 | debian | jdk | updated | repo | 544.7 | 279.5 | 409.9 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 25.0.4.1+8-LTS | 0 (0) | 43 (0) | 47 (0) | 56 (0) |
| corretto | 25 | ubuntu | jdk | updated | repo | 556.4 | 286.3 | 409.9 | Ubuntu 26.04.1 LTS | glibc 2.43 | 25.0.4.1+8-LTS | 0 (0) | 8 (8) | 26 (0) | 4 (0) |
| corretto | 25 | al2023 | jdk | base | official | 551.6 | 244.1 | 349.9 | Amazon Linux 2023.12.20260831 | glibc 2.34 | 25.0.4.1+8-LTS | 0 (0) | 29 (29) | 30 (30) | 0 (0) |
| corretto | 25 | al2023 | jdk | updated | official | 570.0 | 250.2 | 349.9 | Amazon Linux 2023.12.20260914 | glibc 2.34 | 25.0.4.1+8-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| corretto | 25 | al2023 | jre | base | official | 457.1 | 158.3 | 257.5 | Amazon Linux 2023.12.20260831 | glibc 2.34 | 25.0.4.1+8-LTS | 0 (0) | 29 (29) | 30 (30) | 0 (0) |
| corretto | 25 | al2023 | jre | updated | official | 474.9 | 164.4 | 257.5 | Amazon Linux 2023.12.20260914 | glibc 2.34 | 25.0.4.1+8-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| temurin | 17 | alpine | jdk | base | official | 343.0 | 170.3 | 280.4 | Alpine Linux v3.24 | musl 1.2.6 | 17.0.20+8 | 0 (0) | 5 (5) | 11 (11) | 18 (18) |
| temurin | 17 | alpine | jdk | updated | official | 352.3 | 173.7 | 280.4 | Alpine Linux v3.24 | musl 1.2.6 | 17.0.20+8 | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| temurin | 17 | alpine | jre | base | official | 190.2 | 68.0 | 141.5 | Alpine Linux v3.24 | musl 1.2.6 | 17.0.20+8 | 0 (0) | 5 (5) | 11 (11) | 18 (18) |
| temurin | 17 | alpine | jre | updated | official | 199.4 | 71.5 | 141.5 | Alpine Linux v3.24 | musl 1.2.6 | 17.0.20+8 | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| temurin | 17 | debian | jdk | updated | repo | 485.5 | 250.4 | 333.2 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 17.0.20.1+1 | 0 (0) | 45 (0) | 57 (0) | 60 (0) |
| temurin | 17 | debian | jre | updated | repo | 293.9 | 100.3 | 142.2 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 17.0.20.1+1 | 0 (0) | 45 (0) | 57 (0) | 60 (0) |
| temurin | 17 | ubuntu | jdk | base | official | 485.5 | 217.8 | 281.9 | Ubuntu 26.04.1 LTS | glibc 2.43 | 17.0.20+8 | 0 (0) | 8 (8) | 75 (6) | 13 (1) |
| temurin | 17 | ubuntu | jdk | updated | official | 496.1 | 220.6 | 281.9 | Ubuntu 26.04.1 LTS | glibc 2.43 | 17.0.20+8 | 0 (0) | 8 (8) | 69 (0) | 12 (0) |
| temurin | 17 | ubuntu | jre | base | official | 331.0 | 115.6 | 142.4 | Ubuntu 26.04.1 LTS | glibc 2.43 | 17.0.20+8 | 0 (0) | 8 (8) | 75 (6) | 5 (1) |
| temurin | 17 | ubuntu | jre | updated | official | 341.5 | 118.4 | 142.4 | Ubuntu 26.04.1 LTS | glibc 2.43 | 17.0.20+8 | 0 (0) | 8 (8) | 69 (0) | 4 (0) |
| temurin | 21 | alpine | jdk | base | official | 370.5 | 183.6 | 307.8 | Alpine Linux v3.24 | musl 1.2.6 | 21.0.12+8-LTS | 0 (0) | 5 (5) | 11 (11) | 18 (18) |
| temurin | 21 | alpine | jdk | updated | official | 379.8 | 187.1 | 307.8 | Alpine Linux v3.24 | musl 1.2.6 | 21.0.12+8-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| temurin | 21 | alpine | jre | base | official | 213.9 | 74.1 | 165.2 | Alpine Linux v3.24 | musl 1.2.6 | 21.0.12+8-LTS | 0 (0) | 5 (5) | 11 (11) | 18 (18) |
| temurin | 21 | alpine | jre | updated | official | 223.1 | 77.5 | 165.2 | Alpine Linux v3.24 | musl 1.2.6 | 21.0.12+8-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| temurin | 21 | debian | jdk | updated | repo | 514.6 | 265.1 | 362.3 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 21.0.12.1+1-LTS | 0 (0) | 45 (0) | 57 (0) | 60 (0) |
| temurin | 21 | debian | jre | updated | repo | 317.6 | 106.0 | 165.9 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 21.0.12.1+1-LTS | 0 (0) | 45 (0) | 57 (0) | 60 (0) |
| temurin | 21 | ubuntu | jdk | base | official | 512.5 | 230.1 | 308.9 | Ubuntu 26.04.1 LTS | glibc 2.43 | 21.0.12+8-LTS | 0 (0) | 8 (8) | 75 (6) | 13 (1) |
| temurin | 21 | ubuntu | jdk | updated | official | 523.1 | 232.9 | 308.9 | Ubuntu 26.04.1 LTS | glibc 2.43 | 21.0.12+8-LTS | 0 (0) | 8 (8) | 69 (0) | 12 (0) |
| temurin | 21 | ubuntu | jre | base | official | 354.7 | 121.1 | 166.1 | Ubuntu 26.04.1 LTS | glibc 2.43 | 21.0.12+8-LTS | 0 (0) | 8 (8) | 75 (6) | 5 (1) |
| temurin | 21 | ubuntu | jre | updated | official | 365.2 | 124.0 | 166.1 | Ubuntu 26.04.1 LTS | glibc 2.43 | 21.0.12+8-LTS | 0 (0) | 8 (8) | 69 (0) | 4 (0) |
| temurin | 25 | alpine | jdk | base | official | 309.8 | 109.9 | 262.1 | Alpine Linux v3.24 | musl 1.2.6 | 25.0.4+7-LTS | 0 (0) | 5 (5) | 11 (11) | 18 (18) |
| temurin | 25 | alpine | jdk | updated | official | 319.0 | 113.3 | 262.1 | Alpine Linux v3.24 | musl 1.2.6 | 25.0.4+7-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| temurin | 25 | alpine | jre | base | official | 231.5 | 75.5 | 198.5 | Alpine Linux v3.24 | musl 1.2.6 | 25.0.4+7-LTS | 0 (0) | 5 (5) | 11 (11) | 18 (18) |
| temurin | 25 | alpine | jre | updated | official | 240.7 | 78.9 | 198.5 | Alpine Linux v3.24 | musl 1.2.6 | 25.0.4+7-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| temurin | 25 | debian | jdk | updated | repo | 469.8 | 197.3 | 317.6 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 25.0.4.1+1-LTS | 0 (0) | 45 (0) | 57 (0) | 60 (0) |
| temurin | 25 | debian | jre | updated | repo | 352.2 | 116.2 | 200.5 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 25.0.4.1+1-LTS | 0 (0) | 45 (0) | 57 (0) | 60 (0) |
| temurin | 25 | ubuntu | jdk | base | official | 450.4 | 156.7 | 264.7 | Ubuntu 26.04.1 LTS | glibc 2.43 | 25.0.4+7-LTS | 0 (0) | 8 (8) | 59 (6) | 13 (1) |
| temurin | 25 | ubuntu | jdk | updated | official | 460.9 | 159.6 | 264.7 | Ubuntu 26.04.1 LTS | glibc 2.43 | 25.0.4+7-LTS | 0 (0) | 8 (8) | 53 (0) | 12 (0) |
| temurin | 25 | ubuntu | jre | base | official | 371.4 | 123.1 | 200.7 | Ubuntu 26.04.1 LTS | glibc 2.43 | 25.0.4+7-LTS | 0 (0) | 8 (8) | 59 (6) | 5 (1) |
| temurin | 25 | ubuntu | jre | updated | official | 381.9 | 126.0 | 200.7 | Ubuntu 26.04.1 LTS | glibc 2.43 | 25.0.4+7-LTS | 0 (0) | 8 (8) | 53 (0) | 4 (0) |
| zulu | 17 | alpine | jdk | base | official | 297.2 | 151.1 | 281.0 | Alpine Linux v3.23 | musl 1.2.5 | 17.0.20.1+1-LTS | 0 (0) | 2 (2) | 6 (6) | 12 (12) |
| zulu | 17 | alpine | jdk | updated | official | 303.7 | 153.9 | 281.0 | Alpine Linux v3.23 | musl 1.2.5 | 17.0.20.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| zulu | 17 | alpine | jre | base | official | 207.3 | 70.2 | 191.3 | Alpine Linux v3.23 | musl 1.2.5 | 17.0.20.1+1-LTS | 0 (0) | 2 (2) | 6 (6) | 12 (12) |
| zulu | 17 | alpine | jre | updated | official | 213.9 | 72.9 | 191.3 | Alpine Linux v3.23 | musl 1.2.5 | 17.0.20.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| zulu | 17 | debian | jdk | base | official | 389.4 | 181.5 | 281.1 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 17.0.20.1+1-LTS | 3 (3) | 57 (12) | 75 (24) | 81 (21) |
| zulu | 17 | debian | jdk | updated | official | 435.0 | 196.9 | 281.1 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 17.0.20.1+1-LTS | 0 (0) | 45 (0) | 51 (0) | 60 (0) |
| zulu | 17 | debian | jre | base | official | 298.8 | 100.9 | 191.2 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 17.0.20.1+1-LTS | 3 (3) | 57 (12) | 75 (24) | 81 (21) |
| zulu | 17 | debian | jre | updated | official | 344.3 | 116.3 | 191.2 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 17.0.20.1+1-LTS | 0 (0) | 45 (0) | 51 (0) | 60 (0) |
| zulu | 17 | ubuntu | jdk | updated | repo | 440.6 | 205.4 | 281.1 | Ubuntu 26.04.1 LTS | glibc 2.43 | 17.0.20.1+1-LTS | 0 (0) | 8 (8) | 49 (0) | 4 (0) |
| zulu | 17 | ubuntu | jre | updated | repo | 350.0 | 122.8 | 191.2 | Ubuntu 26.04.1 LTS | glibc 2.43 | 17.0.20.1+1-LTS | 0 (0) | 8 (8) | 49 (0) | 4 (0) |
| zulu | 21 | alpine | jdk | base | official | 324.0 | 164.1 | 307.8 | Alpine Linux v3.23 | musl 1.2.5 | 21.0.12.1+1-LTS | 0 (0) | 2 (2) | 6 (6) | 12 (12) |
| zulu | 21 | alpine | jdk | updated | official | 330.5 | 166.9 | 307.8 | Alpine Linux v3.23 | musl 1.2.5 | 21.0.12.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| zulu | 21 | alpine | jre | base | official | 225.1 | 75.3 | 209.1 | Alpine Linux v3.23 | musl 1.2.5 | 21.0.12.1+1-LTS | 0 (0) | 2 (2) | 6 (6) | 12 (12) |
| zulu | 21 | alpine | jre | updated | official | 231.7 | 78.0 | 209.1 | Alpine Linux v3.23 | musl 1.2.5 | 21.0.12.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| zulu | 21 | debian | jdk | base | official | 416.8 | 194.8 | 308.5 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 21.0.12.1+1-LTS | 3 (3) | 57 (12) | 75 (24) | 81 (21) |
| zulu | 21 | debian | jdk | updated | official | 462.5 | 210.2 | 308.5 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 21.0.12.1+1-LTS | 0 (0) | 45 (0) | 51 (0) | 60 (0) |
| zulu | 21 | debian | jre | base | official | 317.1 | 106.2 | 209.5 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 21.0.12.1+1-LTS | 3 (3) | 57 (12) | 75 (24) | 81 (21) |
| zulu | 21 | debian | jre | updated | official | 362.6 | 121.6 | 209.5 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 21.0.12.1+1-LTS | 0 (0) | 45 (0) | 51 (0) | 60 (0) |
| zulu | 21 | ubuntu | jdk | updated | repo | 468.1 | 219.0 | 308.5 | Ubuntu 26.04.1 LTS | glibc 2.43 | 21.0.12.1+1-LTS | 0 (0) | 8 (8) | 49 (0) | 4 (0) |
| zulu | 21 | ubuntu | jre | updated | repo | 368.3 | 128.2 | 209.5 | Ubuntu 26.04.1 LTS | glibc 2.43 | 21.0.12.1+1-LTS | 0 (0) | 8 (8) | 49 (0) | 4 (0) |
| zulu | 25 | alpine | jdk | base | official | 370.3 | 183.9 | 354.2 | Alpine Linux v3.23 | musl 1.2.5 | 25.0.4.1+1-LTS | 0 (0) | 2 (2) | 6 (6) | 12 (12) |
| zulu | 25 | alpine | jdk | updated | official | 376.9 | 186.7 | 354.2 | Alpine Linux v3.23 | musl 1.2.5 | 25.0.4.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| zulu | 25 | alpine | jre | base | official | 266.5 | 89.8 | 250.4 | Alpine Linux v3.23 | musl 1.2.5 | 25.0.4.1+1-LTS | 0 (0) | 2 (2) | 6 (6) | 12 (12) |
| zulu | 25 | alpine | jre | updated | official | 273.0 | 92.5 | 250.4 | Alpine Linux v3.23 | musl 1.2.5 | 25.0.4.1+1-LTS | 0 (0) | 0 (0) | 0 (0) | 0 (0) |
| zulu | 25 | debian | jdk | base | official | 462.5 | 213.9 | 354.2 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 25.0.4.1+1-LTS | 3 (3) | 57 (12) | 75 (24) | 81 (21) |
| zulu | 25 | debian | jdk | updated | official | 508.1 | 229.3 | 354.2 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 25.0.4.1+1-LTS | 0 (0) | 45 (0) | 51 (0) | 60 (0) |
| zulu | 25 | debian | jre | base | official | 358.0 | 120.4 | 250.4 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 25.0.4.1+1-LTS | 3 (3) | 57 (12) | 75 (24) | 81 (21) |
| zulu | 25 | debian | jre | updated | official | 403.5 | 135.8 | 250.4 | Debian GNU/Linux 13 (trixie) | glibc 2.41 | 25.0.4.1+1-LTS | 0 (0) | 45 (0) | 51 (0) | 60 (0) |
| zulu | 25 | ubuntu | jdk | updated | repo | 513.8 | 238.3 | 354.2 | Ubuntu 26.04.1 LTS | glibc 2.43 | 25.0.4.1+1-LTS | 0 (0) | 8 (8) | 49 (0) | 4 (0) |
| zulu | 25 | ubuntu | jre | updated | repo | 409.2 | 142.6 | 250.4 | Ubuntu 26.04.1 LTS | glibc 2.43 | 25.0.4.1+1-LTS | 0 (0) | 8 (8) | 49 (0) | 4 (0) |

## Not available or not built

| Vendor | Java | OS | Flavor | Variant | Status | Reason |
|---|---|---|---|---|---|---|
| oracle | 17 | oraclelinux | jre |  | not-available | Oracle ships no JRE image |
| oracle | 21 | oraclelinux | jre |  | not-available | Oracle ships no JRE image |
| oracle | 25 | oraclelinux | jre |  | not-available | Oracle ships no JRE image |
| redhat | 17 | ubi10-minimal | jdk |  | not-available | RHEL 10 ships OpenJDK 21 and 25 only |
| redhat | 17 | ubi10-minimal | jre |  | not-available | RHEL 10 ships OpenJDK 21 and 25 only |
| redhat | 17 | ubi10 | jdk |  | not-available | RHEL 10 ships OpenJDK 21 and 25 only |
| redhat | 17 | ubi10 | jre |  | not-available | RHEL 10 ships OpenJDK 21 and 25 only |
| microsoft | 17 | azurelinux | jre |  | not-available | Microsoft ships no JRE image or package |
| microsoft | 21 | azurelinux | jre |  | not-available | Microsoft ships no JRE image or package |
| microsoft | 25 | azurelinux | jre |  | not-available | Microsoft ships no JRE image or package |
| corretto | 17 | alpine | jre |  | not-available | Corretto ships JDK packages only on Alpine, Debian and Ubuntu |
| corretto | 17 | debian | jre |  | not-available | Corretto ships JDK packages only on Alpine, Debian and Ubuntu |
| corretto | 17 | ubuntu | jre |  | not-available | Corretto ships JDK packages only on Alpine, Debian and Ubuntu |
| corretto | 21 | alpine | jre |  | not-available | Corretto ships JDK packages only on Alpine, Debian and Ubuntu |
| corretto | 21 | debian | jre |  | not-available | Corretto ships JDK packages only on Alpine, Debian and Ubuntu |
| corretto | 21 | ubuntu | jre |  | not-available | Corretto ships JDK packages only on Alpine, Debian and Ubuntu |
| corretto | 25 | alpine | jre |  | not-available | Corretto ships JDK packages only on Alpine, Debian and Ubuntu |
| corretto | 25 | debian | jre |  | not-available | Corretto ships JDK packages only on Alpine, Debian and Ubuntu |
| corretto | 25 | ubuntu | jre |  | not-available | Corretto ships JDK packages only on Alpine, Debian and Ubuntu |
