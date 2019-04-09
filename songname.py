#!/usr/bin/env python3

# Retrieve's current song and artist name from KEXP, the only radio station I really listen to.

import urllib.request, json


def main():
    req = urllib.request.Request(
        'https://legacy-api.kexp.org/play/?format=json')
    with urllib.request.urlopen(req) as url:
        data = json.loads(url.read().decode())
        print(data['results'][0]['artist']['name'] + ' - ' +
              data['results'][0]['track']['name'])


if __name__ == "__main__":
    main()
