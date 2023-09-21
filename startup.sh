#!/bin/bash

cd $(dirname "$0")

pwd

echo "starting tracker on screen tracker"
screen -d -m -S tracker sh tracker.sh

echo "starting servo controller on screen pituber"
screen -d -m -S pituber sh start.sh

screen -ls