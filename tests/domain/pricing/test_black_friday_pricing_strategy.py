from decimal import Decimal

from proyecto_final.domain.entities.order import Order
from proyecto_final.domain.entities.order_item import OrderItem
from proyecto_final.domain.pricing.black_friday_strategy import (
    BlackFridayPricingStrategy,
)


def test_should_apply_vip_discount():

    strategy = BlackFridayPricingStrategy()

    order = Order(
        customer_name="Alberto",
        items=[
            OrderItem(
                product_name="Keyboard",
                quantity=1,
                price=Decimal("1000.00"),
            )
        ],
    )

    total = strategy.calculate_total(
        order,
    )

    assert total == Decimal("1044.00")
