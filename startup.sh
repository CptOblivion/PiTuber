#!/bin/bash

cd $(dirname "$0")

pwd

echo "starting tracker on screen tracker"
screen -d -S tracker -m /tracker.sh

echo "starting servo controller on screen pituber"
screen -d -S pituber -m ./start.sh