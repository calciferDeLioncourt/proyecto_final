from decimal import Decimal

from proyecto_final.domain.entities.order import Order
from proyecto_final.domain.entities.order_item import OrderItem
from proyecto_final.domain.pricing.regular_pricing_strategy import (
    RegularPricingStrategy,
)


def test_should_calculate_total_with_tax():

    strategy = RegularPricingStrategy()

    order = Order(
        customer_name="Alberto",
        items=[
            OrderItem(
                product_name="Keyboard",
                quantity=2,
                price=Decimal("1000.00"),
            )
        ],
    )

    total = strategy.calculate_total(
        order,
    )

    assert total == Decimal("2320.00")
