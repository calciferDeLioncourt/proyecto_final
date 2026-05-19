from decimal import Decimal

from hypothesis import given
from hypothesis.strategies import decimals

from proyecto_final.domain.entities.order import Order
from proyecto_final.domain.entities.order_item import OrderItem
from proyecto_final.domain.pricing.regular_pricing_strategy import (
    RegularPricingStrategy,
)
from proyecto_final.domain.pricing.vip_pricing_strategy import (
    VipPricingStrategy,
)


@given(
    price=decimals(
        min_value=1,
        max_value=100000,
        places=2,
    )
)
def test_total_should_always_be_positive(
    price,
):
    """
    Total should always
    be positive.
    """

    strategy = RegularPricingStrategy()

    order = Order(
        customer_name="Alberto",
        items=[
            OrderItem(
                product_name="Keyboard",
                quantity=1,
                price=Decimal(price),
            )
        ],
    )

    total = strategy.calculate_total(order)

    assert total > 0


@given(
    price=decimals(
        min_value=1,
        max_value=100000,
        places=2,
    )
)
def test_vip_should_always_be_cheaper_than_regular(
    price,
):

    regular = RegularPricingStrategy()

    vip = VipPricingStrategy()

    order = Order(
        customer_name="Alberto",
        items=[
            OrderItem(
                product_name="Keyboard",
                quantity=1,
                price=Decimal(price),
            )
        ],
    )

    regular_total = regular.calculate_total(order)

    vip_total = vip.calculate_total(order)

    assert vip_total <= regular_total
