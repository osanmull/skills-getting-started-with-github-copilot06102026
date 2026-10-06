import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def activities():
    original_activities = app_module.activities
    isolated_activities = copy.deepcopy(original_activities)
    app_module.activities = isolated_activities

    try:
        yield isolated_activities
    finally:
        app_module.activities = original_activities


@pytest.fixture
def client(activities):
    with TestClient(app_module.app) as test_client:
        yield test_client
