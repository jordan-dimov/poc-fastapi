from fastapi.testclient import TestClient

from app import models
from app.asgi import app, get_db

client = TestClient(app)

test_user_email = "test@pytest"


def _reset_db():
    db = next(get_db())
    db.query(models.User).filter(models.User.email == test_user_email).delete()
    db.commit()


def _create_test_user():
    test_user_data = {
        "email": test_user_email,
        "password": "password123",
    }
    return client.post(
        "/users",
        json=test_user_data,
    )


def test_create_user():
    _reset_db()

    response = _create_test_user()

    assert response.status_code == 200
    resp_user = response.json()
    assert resp_user["email"] == test_user_email
    assert resp_user["id"] > 0
    assert resp_user["is_active"] is True
    assert resp_user["items"] == []


def test_get_user():
    _reset_db()

    response = _create_test_user()
    resp_user = response.json()

    response = client.get("/users/{}".format(resp_user["id"]))
    resp_get_user = response.json()

    assert resp_get_user["email"] == test_user_email
    assert resp_get_user["id"] == resp_user["id"]
    assert resp_get_user["is_active"] is True
    assert resp_get_user["items"] == []


def test_list_users():
    _reset_db()

    response = _create_test_user()
    resp_user = response.json()

    response = client.get("/users")
    resp_list_users = response.json()

    assert len(resp_list_users) >= 1
    user1 = resp_list_users[0]
    assert isinstance(user1["email"], str)
    assert isinstance(user1["is_active"], bool)
    assert isinstance(user1["items"], list)
    assert isinstance(user1["id"], int)
