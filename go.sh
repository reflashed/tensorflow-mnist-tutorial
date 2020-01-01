#!/bin/bash

docker build . -t tensorflow-mnist-tutorial
docker run --rm -it \
  -e DISPLAY=$DISPLAY \
  -v $XAUTHORITY:/root/.Xauthority \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v ${PWD}:/app \
  tensorflow-mnist-tutorial bash
