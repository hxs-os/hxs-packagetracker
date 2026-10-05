FROM alpine:latest AS build
WORKDIR /packagetracker

RUN apk add \
    build-base \
    meson \
    ninja \
    pkgconf \
    sqlite-dev \
    sqlite-static \
    cmake \
    libarchive-dev \
    libarchive-static \
    acl-dev \
    acl-static \
    expat-dev \
    expat-static \
    lz4-dev \
    lz4-static \
    bzip2-dev \
    bzip2-static \
    zlib-dev \
    zlib-static \
    xz-dev \
    xz-static \
    openssl-dev \
    openssl-libs-static \
    zstd-dev \
    zstd-static \
    binutils \
    libedit \
    libedit-static \
    libedit-dev \
    git \
    fakeroot

RUN git clone https://git.sr.ht/~juanvel400/xpt /xpt-src --depth=1
COPY . .
RUN find . -type f -name '*.ebs' -print0 | xargs -0 -n1 /xpt-src/ebt/ebs.sh build

FROM scratch AS artifacts

COPY --from=build /packagetracker /artifacts
