"""
Domain order item entity.
"""

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class OrderItem:
    """
    Entidad item de orden.
    """

    product_name: str

    quantity: int

    price: Decimal

    id: int | None = None
