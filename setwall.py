#!/usr/bin/env python3

# setwall.py by Valkyrie
#
# Uses pywal to set a random background and terminal color scheme

import pywal, os
def main():
    papedir = os.environ['HOME'] + "/.papes"
    wallpaper = pywal.image.get(papedir)
    colors = pywal.colors.get(wallpaper)

    pywal.wallpaper.change(wallpaper)
    pywal.sequences.send(colors)

    pywal.reload.env()

main()
