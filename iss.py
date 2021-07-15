#!/usr/bin/env python

__author__ = 'Rebekah Eloise Miller with help from Matt Perry'

import requests


def num_astros():
    r = requests.get("http://api.open-notify.org/astros.json")
    print(r.status_code)
    print(r.json())


def current_loc():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    print(r.status_code)
    print(r.json())


def main():
    num_astros()
    current_loc()


if __name__ == '__main__':
    main()
