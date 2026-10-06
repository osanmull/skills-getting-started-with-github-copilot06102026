from src import app as app_module


def test_participant_can_be_added_to_an_activity(client, activities):
    # Arrange
    activity_name = "Chess Club"
    email = "new-student@example.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == (
        f"Signed up {email} for {activity_name}"
    )
    assert email in activities[activity_name]["participants"]


def test_unknown_activity_returns_not_found(client):
    # Arrange
    activity_name = "Unknown Activity"
    email = "student@example.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_student_cannot_sign_up_twice_for_the_same_activity(client, activities):
    # Arrange
    activity_name = "Chess Club"
    email = "repeat-student@example.edu"
    activities[activity_name]["participants"].append(email)

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == (
        "Student is already signed up for this activity"
    )
    assert activities[activity_name]["participants"].count(email) == 1
