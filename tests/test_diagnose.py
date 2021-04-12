"""
Tests for diagnose.py
"""

import pytest
import requests
import requests_mock
from diagnose import diagnose

STATUS_ENDPOINT = "https://code-exercise-api.buffer.com/cluster/status.json"
STATUS_MOCK_MISS = {"pods": [{"name": "something_else", "status": "RUNNING"}]}
STATUS_MOCK_CLBO = {"pods": [{"name": "mock-1", "status": "CrashLoopBackOff"}]}
STATUS_MOCK_IPBO = {"pods": [{"name": "mock-1", "status": "ImagePullBackOff"}]}


def test_status(requests_mock):
    requests_mock.get(STATUS_ENDPOINT, json={"name": "mock"})
    response = diagnose.status()
    assert response == {"name": "mock"}


def test_check_miss():
    expected_status_miss = (
        'No pods were found matching "mock". The item you are looking '
        + "for may not have been deployed."
    )
    status_miss = diagnose.check(STATUS_MOCK_MISS, "mock")
    assert status_miss == expected_status_miss


def test_check_clbo():
    expected_status_clbo = (
        '1 items with state "CrashLoopBackOff" found matching "mock"\n'
        + "CrashLoopBackOff: Unable to start this pod due to a code error"
    )
    print(expected_status_clbo)
    status_clbo = diagnose.check(STATUS_MOCK_CLBO, "mock")
    assert status_clbo == expected_status_clbo


def test_check_ipbo():
    expected_status_ipbo = (
        '1 items with state "ImagePullBackOff" found matching "mock"\n'
        + "ImagePullBackOff: Unable to pull the image specified for this pod"
    )
    status_ipbo = diagnose.check(STATUS_MOCK_IPBO, "mock")
    assert status_ipbo == expected_status_ipbo
