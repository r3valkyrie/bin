#!/bin/bash

INITFILE=/tmp/.init

# Start some programs on first launch

if [ ! -f $INITFILE ]; then
	touch $INITFILE
	tmux new-session -d -s 'misc' -n 'irc' 'irssi'
	tmux new-window -t 'misc' -n 'music' 'ncmpcpp'

    # Clean home directory a bit
    setopt +o nomatch

    for a in $HOME/*.{txt,docx,odt}; do
        mv $a $HOME/doc/unsorted/ > /dev/null 2>&1;
    done

    for b in $HOME/*.{mp4,mov,avi,webm}; do
        mv $b $HOME/vid/unsorted/ > /dev/null 2>&1;
    done

    for c in $HOME/*.{jpg,jpeg,png,gif,svg,webp}; do
        mv $c $HOME/img/unsorted/ > /dev/null 2>&1;
    done

    for d in $HOME/*.{mp3,wav}; do
        mv $d $HOME/mp3/unsorted/ > /dev/null 2>&1;
    done

    for e in $HOME/*.tmp; do
        mv $e /tmp/ > /dev/null 2>&1;
    done

    for f in $HOME/*.iso; do
        mv $f $HOME/iso/ > /dev/null 2>&1;
    done
fi
