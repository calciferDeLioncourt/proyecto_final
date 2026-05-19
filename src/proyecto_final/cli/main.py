import json
import os
from pathlib import Path

import requests
import typer
from dotenv import load_dotenv

load_dotenv()

app = typer.Typer()

BASE_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000",
)

TOKEN_FILE = Path.home() / ".orders_cli_token.json"


def save_token(token: str):

    TOKEN_FILE.write_text(
        json.dumps(
            {
                "access_token": token,
            }
        )
    )


def load_token() -> str:

    if not TOKEN_FILE.exists():

        typer.echo("You are not authenticated. " "Run login first.")

        raise typer.Exit(code=1)

    data = json.loads(TOKEN_FILE.read_text())

    return data["access_token"]


def get_auth_headers():

    token = load_token()

    return {"Authorization": f"Bearer {token}"}


@app.command()
def login(
    username: str,
    password: str,
):

    payload = {
        "username": username,
        "password": password,
    }

    response = requests.post(
        f"{BASE_URL}/auth/login",
        json=payload,
    )

    if response.status_code != 200:

        typer.echo("Invalid credentials")

        raise typer.Exit(code=1)

    token = response.json()["access_token"]

    save_token(token)

    typer.echo("Login successful")


@app.command()
def list_orders(
    strategy: str = "regular",
):

    response = requests.get(
        f"{BASE_URL}/orders/{strategy}",
        headers=get_auth_headers(),
    )

    if response.status_code != 200:

        typer.echo(f"Error retrieving orders: " f"{response.status_code}")

        typer.echo(response.text)

        raise typer.Exit(code=1)

    orders = response.json()

    if not orders:

        typer.echo("No orders found")

        return

    for order in orders:

        typer.echo(
            f"ID: {order['id']} | "
            f"Customer: {order['customer_name']} | "
            f"Total: {order['total']}"
        )


@app.command()
def create_order(
    customer_name: str,
):

    payload = {
        "customer_name": customer_name,
        "items": [
            {
                "product_name": "Keyboard",
                "quantity": 1,
                "price": 100,
            }
        ],
    }

    response = requests.post(
        f"{BASE_URL}/orders",
        json=payload,
        headers=get_auth_headers(),
    )

    if response.status_code != 200:

        typer.echo(f"Error creating order: " f"{response.status_code}")

        typer.echo(response.text)

        raise typer.Exit(code=1)

    typer.echo("Order created successfully")

    typer.echo(response.json())


@app.command()
def delete_order(
    order_id: int,
):

    response = requests.delete(
        f"{BASE_URL}/orders/{order_id}",
        headers=get_auth_headers(),
    )

    if response.status_code != 200:

        typer.echo(f"Error deleting order: " f"{response.status_code}")

        typer.echo(response.text)

        raise typer.Exit(code=1)

    typer.echo("Order deleted successfully")


@app.command()
def get_order_by_id(
    order_id: int,
    strategy: str = "regular",
):

    response = requests.get(
        f"{BASE_URL}/orders/{order_id}/{strategy}",
        headers=get_auth_headers(),
    )

    if response.status_code != 200:

        typer.echo(f"Error get order: " f"{response.status_code}")

        typer.echo(response.text)

        raise typer.Exit(code=1)

    order = response.json()

    if not order:

        typer.echo("No orders found")

        return

    typer.echo(
        f"ID: {order['id']} | "
        f"Customer: {order['customer_name']} | "
        f"Total: {order['total']}"
    )


if __name__ == "__main__":
    app()
