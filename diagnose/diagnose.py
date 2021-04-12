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

    parser.add_argument(
        "--check",
        "-c",
        help="Get the status a service with provided prefix.",
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
        sys.exit(1)
    except Exception as err:
        print(f"Other error occurred: {err}")
        sys.exit(1)


def check(status, check_item):
    """
    Check the status for a specific type of item (by prefix).
    :returns: a string containing the number of items matching and an
              explanation of the status.
    """
    states = {}
    state_descriptions = {
        "ImagePullBackOff": "Unable to pull the image specified for this pod",
        "CrashLoopBackOff": "Unable to start this pod due to a code error",
        "RUNNING": "Pod is working as expected",
    }

    for pod in status["pods"]:
        if pod["name"].startswith(check_item):
            states.setdefault(pod["status"], []).append(pod["name"])

    if len(states) == 0:
        return (
            f'No pods were found matching "{check_item}". The item you are '
            + "looking for may not have been deployed."
        )

    for state in states:
        message = (
            f'{len(states[state])} items with state "{state}" found matching '
            + f'"{check_item}"\n'
        )
        try:
            message += f"{state}: {state_descriptions[state]}"
        except:
            message += f"No description available for {state}"
        return message


def main():
    """
    Where things get done.
    """
    arg = arguments()

    if arg.get:
        print(status())

    if arg.check != None:
        diagnosis = check(status(), arg.check)
        print(diagnosis)

    sys.exit(0)


if __name__ == "__main__":
    """
    To allow being called as a script, if installing as a CLI is not desired.
    """
    main()
