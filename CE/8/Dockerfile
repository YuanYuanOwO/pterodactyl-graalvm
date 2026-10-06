# ----------------------------------
# Pterodactyl Core Dockerfile
# Environment: Java
# Minimum Panel Version: 1.7.0
# ----------------------------------
FROM debian:bookworm-slim

ARG GRAAL_VERSION=21.3.1
ARG JAVA_VERSION=8

LABEL maintainer="Tommaso Benatti <tommaso.benatti@outlook.com>"

ENV DEBIAN_FRONTEND=noninteractive

# Default to UTF-8 file.encoding
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

RUN apt-get update -y \
  && apt-get install -y --no-install-recommends bash coreutils sed unzip \
      apt-transport-https \
      apt-utils \
      ca-certificates \
      curl \
      fontconfig \
      git \
      gnupg2 \
      iproute2 \
      jq \
      java-common \
      locales \
      openssl \
      procps \
      sqlite3 \
      tar \
      tzdata \
      wget \
      libfreetype6 \
      build-essential \
      zlib1g-dev \
  && echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
  && locale-gen en_US.UTF-8 \
  && GRAALVM_URL="https://github.com/graalvm/graalvm-ce-builds/releases/download/vm-${GRAAL_VERSION}/graalvm-ce-java${JAVA_VERSION}-linux-amd64-${GRAAL_VERSION}.tar.gz" \
  && curl --proto "=https" --proto-redir "=https" --retry 3 --retry-all-errors --connect-timeout 15 --max-time 600 -Lfso /tmp/graalvm.tar.gz "${GRAALVM_URL}" \
  && curl --proto "=https" --proto-redir "=https" --retry 3 --retry-all-errors --connect-timeout 15 --max-time 120 -Lfso /tmp/graalvm.sha256 "${GRAALVM_URL}.sha256" \
  && printf '%s  %s\n' "$(awk '{print $1}' /tmp/graalvm.sha256)" /tmp/graalvm.tar.gz | sha256sum -c - \
  && mkdir -p /opt/java/graalvm \
  && cd /opt/java/graalvm \
  && tar -xf /tmp/graalvm.tar.gz --strip-components=1 \
  && export PATH="/opt/java/graalvm/bin:$PATH" \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /tmp/graalvm.tar.gz /tmp/graalvm.sha256

ENV JAVA_HOME=/opt/java/graalvm \
    PATH="/opt/java/graalvm/bin:$PATH"

# Step 2 - add pterodactyl stuff
RUN useradd -d /home/container -m container

USER        container
ENV         USER=container HOME=/home/container

WORKDIR     /home/container

COPY entrypoint.sh /entrypoint.sh

CMD         ["/bin/bash", "/entrypoint.sh"]