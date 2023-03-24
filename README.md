# PiTuber
Raspberry Pi Vtuber avatar for real life

Raspberry Pi controller for a phyiscal vtuber avatar; requires a webcam and servos for the puppet

This is mostly just messing around and trying to kludge together something that works, no promises that it'll turn into anything

Requirements (tentative, changing)

- tracking software: https://github.com/emilianavt/OpenSeeFace
  - this requires ONNX runtime - pip can't find wheel for pi, instead get it from https://github.com/nknytk/built-onnxruntime-for-raspberrypi-linux
    - navigate to corresponding directory for the debian version, and `pip install` your wheel file
  - may need to `sudo apt-get install libatlas-base-dev` for numpy