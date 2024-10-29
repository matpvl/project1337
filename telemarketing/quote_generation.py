"""File containing functions for generating random quotes."""

import json
import sys

import requests


def miss_the_old_kanye() -> str:
    """Return new Kanye West quote."""
    url = "https://api.kanye.rest"
    r = requests.get(url, timeout=60)
    sys.stdout.write("Fetching quote...\n")
    return str(json.loads(r.text))
