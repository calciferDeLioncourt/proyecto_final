from decimal import Decimal

from proyecto_final.application.use_cases.get_order_by_id_use_case import (
    GetOrderByIdUseCase,
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

    def get_order_by_id(self, order_id: int) -> Order | None:

        return Order(
            id=order_id,
            customer_name="Alberto",
            items=[
                OrderItem(
                    id=1,
                    product_name="Keyboard",
                    quantity=2,
                    price=Decimal("1000.00"),
                )
            ],
        )


def test_should_get_order_by_id_with_total():
    """
    Should return orders
    with calculated totals.
    """

    repository = FakeOrderRepository()

    strategy = RegularPricingStrategy()

    use_case = GetOrderByIdUseCase(
        repository=repository,
        pricing_strategy=strategy,
    )

    result = use_case.execute(order_id=1)

    assert result is not None

    assert result.id == 1

    assert result.total == (Decimal("2320.00"))
