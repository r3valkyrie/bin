#!/usr/bin/env python3

# Retrieve's current song and artist name from KEXP, the only radio station I really listen to.

import requests


def main():
    url = 'https://legacy-api.kexp.org/play/?format=json'
    r = requests.get(url)
    data = r.json()
    print(data['results'][0]['artist']['name'] + ' - ' +
          data['results'][0]['track']['name'])


if __name__ == "__main__":
    main()
