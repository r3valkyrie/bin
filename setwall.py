#!/usr/bin/env python3

# setwall.py by Valkyrie
#
# Uses pywal to set a random background and terminal color scheme

import pywal, os
def main():
    papedir = os.environ['HOME'] + "/.papes"
    wallpaper = pywal.image.get(papedir)
    colors = pywal.colors.get(wallpaper)

    pywal.sequences.send(colors)

    pywal.export.every(colors)

    pywal.reload.env()
    pywal.reload.xrdb()

    pywal.wallpaper.change(wallpaper)

    os.system('/usr/local/bin/wal-discord -t > /dev/null')
    os.system('/usr/local/bin/wal-steam > /dev/null')
main()
