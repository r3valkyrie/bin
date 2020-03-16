#!/bin/bash

# Set brightness for my dumb monitors.


if [[ $EUID -ne 0 ]]; then
    echo "You need to be root, unfortunately."
    exit 1
fi

if [ "$1" != "" ]; then
    echo "Changing backlight setting to $1..."

    # Laptop monitor

    echo "Setting brightness for laptop screen"
    xbacklight -set "$1" > /dev/null
    
    for x in {1..2}; do
        i=0
        while true; do
            errlog=$(mktemp)
            echo "Setting brightness for Display $x"

    # Sometimes it randomly fails verification for no reason. Solution is to do it again.

            ddcutil setvcp -d $x 10 "$1" >/dev/null 2>$errlog
            if [ ! -s $errlog ]; then
                rm "$errlog"
                break
            fi
            echo "Retrying..."
        done
    done
fi
