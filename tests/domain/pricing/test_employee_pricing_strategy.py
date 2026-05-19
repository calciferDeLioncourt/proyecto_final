from decimal import Decimal

from proyecto_final.domain.entities.order import Order
from proyecto_final.domain.entities.order_item import OrderItem
from proyecto_final.domain.pricing.employee_pricing_strategy import (
    EmployeePricingStrategy,
)


def test_should_apply_vip_discount():

    strategy = EmployeePricingStrategy()

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

    assert total == Decimal("870.00")
