#!/usr/bin/env python3

# Sets the title of a urxvt terminal

import sys

title = " ".join(sys.argv[1:])

sys.stdout.write("\x1b]2;" + title + "\x07")
