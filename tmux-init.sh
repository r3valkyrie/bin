#!/bin/bash

INITFILE=/tmp/.tmux-init

# Start some programs on first launch

if [ ! -f $INITFILE ]; then
	touch /tmp/.tmux-init
	tmux new-session -d -s 'misc' -n 'irc' 'irssi'
	tmux new-window -t 'misc' -n 'music' 'pms -H /tmp/mpd.socket'
    tmux new-window -t 'misc' -n 'mail' 'neomutt'
fi
