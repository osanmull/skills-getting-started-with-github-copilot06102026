from fastapi.testclient import TestClient

from src.app import activities, app


def test_participant_can_be_unregistered_from_an_activity():
    activity_name = "Chess Club"
    email = "student@example.edu"
    activities[activity_name]["participants"].append(email)
    client = TestClient(app)

    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )

    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]


def test_unregistered_participant_returns_an_error():
    activity_name = "Chess Club"
    email = "missing@example.edu"
    client = TestClient(app)

    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )

    assert response.status_code == 400
    assert "not signed up" in response.json()["detail"].lower()
