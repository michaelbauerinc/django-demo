#!/bin/bash
IMAGE=$(docker images static_ubuntu --format "{{.Repository}}")
if [ "$IMAGE" ]; then
    echo "Found base image. No need to build.";

    exit 0;
fi

docker build . -t static_ubuntu