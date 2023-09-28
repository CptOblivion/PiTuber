# PiTuber
Raspberry Pi Vtuber avatar for real life

Raspberry Pi controller for a phyiscal vtuber avatar; requires a webcam and servos for the puppet

This is mostly just messing around and trying to kludge together something that works, no promises that it'll turn into anything

Requirements (tentative, changing)

Running OpenSeeFace on a raspberry pi, even with lowest tracking quality, is pretty slow (~4fps on a pi 3). Probably not worth doing.
- tracking software: https://github.com/emilianavt/OpenSeeFace
  - this requires ONNX runtime - pip can't find wheel for pi, instead get it from https://github.com/nknytk/built-onnxruntime-for-raspberrypi-linux
    - navigate to corresponding directory for the debian version, and `pip install` your wheel file
  - numpy:
    - may need to `sudo apt-get install libatlas-base-dev`
    - raspberry pi 4:
      ```
      sudo apt-get update
      sudo apt-get install python3-pkgconfig libopenblas-dev
      ```
  - opencv might take too long to insall, try this: https://singleboardblog.com/install-python-opencv-on-raspberry-pi/
  - for raspberry pi local run, `sudo pip3 install adafruit-circuitpython-servokit`
    - don't forget to enable I2C:
      - `sudo raspi-config` -> Interface Options -> I2C

Alternately, run OpenSeeFace on a PC and send the socket to the pi:
- when starting OpenSeeFace, use the `-i` argument, with the IP address of the pi that will be reading the tracking data.

TODO:
- optional motor speed limit
- auto-calibrate center
  - at startup
  - triggerable?
- smoothing