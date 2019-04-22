#!/usr/bin/env python3

# setwall.py by Valkyrie
#
# Uses pywal to set a random background and terminal color scheme

import pywal, os, re, yaml


def main():
    papedir = os.environ['HOME'] + "/.papes"
    wallpaper = pywal.image.get(papedir)
    colors = pywal.colors.get(wallpaper)

    pywal.sequences.send(colors)

    pywal.export.every(colors)

    pywal.reload.env()
    pywal.reload.xrdb()

    pywal.wallpaper.change(wallpaper)

    # Hacky way to set budgie-panel's background color.
    # It doesn't want to let me import pywal's colors.css for some reason.
    budgie_css = open(os.environ['HOME'] + '/.config/gtk-3.0/gtk.css',
                      'r').read()
    budgie_css_writeto = open(os.environ['HOME'] + '/.config/gtk-3.0/gtk.css',
                              'w')
    colors_yaml = yaml.safe_load(
        open(os.environ['HOME'] + '/.cache/wal/colors.yml'))

    content_new = re.sub(
        r"background-color: (.*);", "background-color: {};".format(
            colors_yaml['special']['background']), budgie_css)
    budgie_css_writeto.write(content_new)
    budgie_css_writeto.close()

    print(content_new)

    os.system('/usr/local/bin/wal-steam > /dev/null')
    os.system('budgie-panel --replace &')


main()
