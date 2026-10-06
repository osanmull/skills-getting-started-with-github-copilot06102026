def test_participant_can_be_unregistered_from_an_activity(client, activities):
    # Arrange
    activity_name = "Chess Club"
    email = "student@example.edu"
    activities[activity_name]["participants"].append(email)

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == (
        f"Unregistered {email} from {activity_name}"
    )
    assert email not in activities[activity_name]["participants"]


def test_unknown_activity_returns_not_found_when_unregistering(client):
    # Arrange
    activity_name = "Unknown Activity"
    email = "student@example.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregistered_participant_returns_an_error(client, activities):
    # Arrange
    activity_name = "Chess Club"
    email = "missing@example.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == (
        "Student is not signed up for this activity"
    )
    assert email not in activities[activity_name]["participants"]
