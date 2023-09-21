#!/bin/bash

cd $(dirname "$0")

screen -d -S tracker -m /tracker.sh

screen -d -S pituber -m ./start.sh