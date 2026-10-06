from src import app as app_module


def test_root_redirects_to_the_static_frontend(client):
    # Arrange
    expected_redirect = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == expected_redirect


def test_get_activities_returns_the_current_activity_data(client, activities):
    # Arrange
    activity_name = "Chess Club"
    expected_participants = activities[activity_name]["participants"]

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.json()[activity_name]["participants"] == expected_participants
