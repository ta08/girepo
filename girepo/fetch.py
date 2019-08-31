#!/usr/bin/env python

import requests
from datetime import datetime

BASE_URL = "https://api.github.com/repos"


def fetch_from(full_name: str):
    full_url = '/'.join([BASE_URL, full_name])
    return fetch(full_url)


def fetch(url: str):
    with requests.get(url) as response:
        json = response.json()
        if response.status_code is not 200:
            json['status_code'] = response.status_code
            timestamp = int(response.headers['X-RateLimit-Reset'])
            json['X-RateLimit-Reset'] = datetime.fromtimestamp(timestamp).isoformat()
        return response.status_code, json
