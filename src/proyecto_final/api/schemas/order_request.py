"""
Schemas relacionados con órdenes.
"""

from decimal import Decimal

from pydantic import BaseModel, Field


class OrderItemCreateSchema(BaseModel):
    """
    Schema creación item.
    """

    product_name: str = Field(
        min_length=3,
        max_length=100,
    )

    quantity: int = Field(
        gt=0,
    )

    price: Decimal = Field(
        gt=0,
    )


class OrderCreateSchema(BaseModel):
    """
    Schema creación orden.
    """

    customer_name: str = Field(
        min_length=3,
        max_length=100,
    )

    items: list[OrderItemCreateSchema] = Field(
        min_length=1,
    )
