from decimal import Decimal

from proyecto_final.application.use_cases.get_orders_use_case import (
    GetOrdersUseCase,
)
from proyecto_final.domain.entities.order import Order
from proyecto_final.domain.entities.order_item import OrderItem
from proyecto_final.domain.pricing.regular_pricing_strategy import (
    RegularPricingStrategy,
)


class FakeOrderRepository:
    """
    Fake repository for tests.
    """

    def get_orders(
        self,
    ) -> list[Order]:

        return [
            Order(
                id=1,
                customer_name="Alberto",
                items=[
                    OrderItem(
                        id=1,
                        product_name="Keyboard",
                        quantity=2,
                        price=Decimal("1000.00"),
                    )
                ],
            ),
            Order(
                id=2,
                customer_name="Calcifer",
                items=[
                    OrderItem(
                        id=2,
                        product_name="Mouse",
                        quantity=1,
                        price=Decimal("500.00"),
                    )
                ],
            ),
        ]


def test_should_get_orders_with_total():
    """
    Should return orders
    with calculated totals.
    """

    repository = FakeOrderRepository()

    strategy = RegularPricingStrategy()

    use_case = GetOrdersUseCase(
        repository=repository,
        pricing_strategy=strategy,
    )

    result = use_case.execute()

    assert len(result) == 2

    assert result[0].total == (Decimal("2320.00"))

    assert result[1].total == (Decimal("580.00"))
