from decimal import Decimal

from proyecto_final.application.use_cases.create_order_use_case import (
    CreateOrderUseCase,
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

    def __init__(self):

        self.orders = []

    def create_order(
        self,
        order: Order,
    ) -> Order:

        order.id = 1

        self.orders.append(
            order,
        )

        return order


class FakeNotificationService:
    """
    Fake notification adapter.
    """

    def __init__(self):

        self.notifications_sent = 0

    def send_order_created(
        self,
        order: Order,  # noq F401
    ) -> None:

        self.notifications_sent += 1


def test_should_create_order():

    repository = FakeOrderRepository()

    strategy = RegularPricingStrategy()

    use_case = CreateOrderUseCase(
        repository=repository,
        pricing_strategy=strategy,
    )

    order = Order(
        customer_name="Alberto_test",
        items=[
            OrderItem(
                product_name="Keyboard",
                quantity=2,
                price=Decimal("1000.00"),
            )
        ],
    )

    result = use_case.execute(
        order,
    )

    assert result.id == 1

    assert result.total == (Decimal("2320.00"))

    assert len(repository.orders) == 1
