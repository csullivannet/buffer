#!/usr/bin/env python3
"""
Author: Christopher Sullivan
Description: Take-home test for buffer. A command line tool to get the response
from a status endpoint and provide feedback to the user.
"""

import argparse
import json
import requests
import sys
from requests.exceptions import HTTPError

STATUS_ENDPOINT = "https://code-exercise-api.buffer.com/cluster/status.json"


def arguments():
    """
    A handler for command line arguments.
    :returns: arguments passed at the command line.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--get",
        "-g",
        action="store_true",
        help="Get the status of the cluster and print raw response.",
    )

    return parser.parse_args()


def status():
    """
    A simple request on the STATUS_ENDPOINT.
    :returns: the content of the endpoint response as a json object.
    """
    try:
        response = requests.get(STATUS_ENDPOINT)
        response.raise_for_status()
        jsonResponse = response.json()
        return jsonResponse

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


def main():
    """
    Where things get done.
    """
    arg = arguments()

    if arg.get:
        print(status())
        sys.exit(0)


if __name__ == "__main__":
    """
    To allow being called as a script, if installing as a CLI is not desired.
    """
    main()
