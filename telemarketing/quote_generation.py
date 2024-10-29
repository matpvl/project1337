"""File containing functions for generating random quotes."""
import json
import sys

import requests


def miss_the_old_kanye() -> str:
    """Returns a new Kanye West quote."""
    url="https://api.kanye.rest"
    r = requests.get(url)
    sys.stdout.write("Fetching quote...\n")
    return json.loads(r.text)
