"""
Create order DTO.
"""

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CreateOrderDTO:
    """
    Datos creación orden.
    """

    customer_name: str

    total: Decimal
