"""
Tests for diagnose.py
"""

import pytest
import requests
import requests_mock
from diagnose import diagnose

STATUS_ENDPOINT = "https://code-exercise-api.buffer.com/cluster/status.json"


def test_status(requests_mock):
    requests_mock.get(STATUS_ENDPOINT, json={"name": "mock"})
    response = diagnose.status()
    assert response == {"name": "mock"}
