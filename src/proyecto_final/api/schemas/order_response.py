from decimal import Decimal

from pydantic import BaseModel


class OrderItemResponseSchema(BaseModel):
    """
    Schema respuesta item.
    """

    id: int
    product_name: str
    quantity: int
    price: Decimal

    model_config = {
        "from_attributes": True,
    }


class OrderResponseSchema(BaseModel):
    """
    Schema respuesta orden.
    """

    id: int
    customer_name: str
    items: list[OrderItemResponseSchema]
    total: Decimal

    model_config = {
        "from_attributes": True,
    }
