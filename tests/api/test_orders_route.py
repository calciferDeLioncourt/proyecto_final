from fastapi.testclient import TestClient

from proyecto_final.api.main import app

client = TestClient(app)


def get_auth_headers():

    login_payload = {
        "username": "admin",
        "password": "123456",
    }

    response = client.post(
        "/auth/login",
        json=login_payload,
    )

    token = response.json()["access_token"]

    return {"Authorization": f"Bearer {token}"}


def test_should_get_order_by_id():
    payload = {
        "customer_name": "Alberto",
        "items": [
            {
                "product_name": "Keyboard",
                "quantity": 2,
                "price": "1000.00",
            }
        ],
    }

    create_response = client.post(
        "/orders",
        json=payload,
        headers=get_auth_headers(),
    )

    created_order = create_response.json()

    order_id = created_order["id"]

    response = client.get(
        f"/orders/{order_id}/regular",
        headers=get_auth_headers(),
    )

    assert response.status_code == 200


def test_should_delete_order_by_id():
    payload = {
        "customer_name": "Alberto",
        "items": [
            {
                "product_name": "Keyboard",
                "quantity": 2,
                "price": "1000.00",
            }
        ],
    }

    create_response = client.post(
        "/orders",
        json=payload,
        headers=get_auth_headers(),
    )

    created_order = create_response.json()

    order_id = created_order["id"]

    response = client.delete(
        f"/orders/{order_id}",
        headers=get_auth_headers(),
    )

    assert response.status_code == 200


def test_should_get_orders():

    response = client.get(
        "/orders/regular",
        headers=get_auth_headers(),
    )

    assert response.status_code == 200


def test_should_create_order():

    payload = {
        "customer_name": "Alberto_test",
        "items": [
            {
                "product_name": "Keyboard",
                "quantity": 2,
                "price": "1000.00",
            }
        ],
    }

    response = client.post(
        "/orders",
        json=payload,
        headers=get_auth_headers(),
    )

    assert response.status_code == 200
