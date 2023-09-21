#!/bin/bash

path = $(dirname "$0")

screen -d -S tracker -m "$path/tracker.sh"

screen -d -S pituber -m "$path/start.sh"