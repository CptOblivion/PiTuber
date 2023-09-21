#!/bin/bash

cd $(dirname "$0")

pwd

echo "starting tracker on screen tracker"
screen -d -m -S tracker bash -c "./tracker.sh; exec sh"

echo "starting servo controller on screen pituber"
screen -d -m -S pituber bash -c "./start.sh; exec sh"

screen -ls