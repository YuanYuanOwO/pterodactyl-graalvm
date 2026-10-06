# ----------------------------------
# Pterodactyl Core Dockerfile
# Environment: Oracle GraalVM JDK 17
# Minimum Panel Version: 1.7.0
# ----------------------------------
FROM container-registry.oracle.com/graalvm/jdk:17 AS graalvm
FROM debian:trixie-slim

LABEL maintainer="Tommaso Benatti <tommaso.benatti@outlook.com>" \
      org.opencontainers.image.source="https://github.com/tommasobenatti/pterodactyl-graalvm" \
      org.opencontainers.image.licenses="MIT"

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends coreutils sed unzip \
        bash \
        ca-certificates \
        curl \
        fontconfig \
        git \
        iproute2 \
        jq \
        libfreetype6 \
        libstdc++6 \
        locales \
        lsof \
        openssl \
        procps \
        sqlite3 \
        tar \
        tzdata \
    && echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
    && locale-gen en_US.UTF-8 \
    && useradd -d /home/container -m container \
    && rm -rf /var/lib/apt/lists/*

COPY --from=graalvm /usr/lib64/graalvm/graalvm-java17 /opt/java/graalvm

ENV JAVA_HOME=/opt/java/graalvm \
    PATH="/opt/java/graalvm/bin:${PATH}"

USER container
ENV USER=container HOME=/home/container
WORKDIR /home/container

COPY entrypoint.sh /entrypoint.sh

CMD ["/bin/bash", "/entrypoint.sh"]
