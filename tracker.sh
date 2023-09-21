#!/bin/bash

path = $(dirname "$0")

cd "$path/../OpenSeeFace"
python3 facetracker.py --gaze-tracking 0 --model -3