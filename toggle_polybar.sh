#!/bin/bash

if [[ $(pidof polybar) ]]; then
    pkill polybar
else
    $HOME/.bin/launch_polybar.sh
fi
