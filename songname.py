#!/usr/bin/env python3

# Retrieve's current song and artist name from KEXP, the only radio station I really listen to.

import urllib.request, json


def main():
    url = 'https://legacy-api.kexp.org/play/?format=json'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as url: #nosec
        data = json.loads(url.read().decode())
        print(data['results'][0]['artist']['name'] + ' - ' +
                data['results'][0]['track']['name'])


if __name__ == "__main__":
    main()
