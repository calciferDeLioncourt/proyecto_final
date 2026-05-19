"""
Domain order entity.
"""

from dataclasses import dataclass
from decimal import Decimal

from proyecto_final.domain.entities.order_item import OrderItem


@dataclass
class Order:
    """
    Entidad orden.
    """

    customer_name: str

    items: list["OrderItem"]

    id: int | None = None

    total: Decimal | None = None
