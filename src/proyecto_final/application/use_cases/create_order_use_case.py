from proyecto_final.domain.entities.order import Order
from proyecto_final.domain.ports.order_repository_port import (
    OrderRepositoryPort,
)
from proyecto_final.domain.pricing.pricing_strategy import (
    PricingStrategy,
)


class CreateOrderUseCase:
    """
    Caso uso crear orden.
    """

    def __init__(
        self,
        repository: OrderRepositoryPort,
        pricing_strategy: PricingStrategy,
    ) -> None:

        self._repository = repository
        self._pricing_strategy = pricing_strategy

    def execute(
        self,
        order: Order,
    ) -> Order:
        """
        Ejecuta caso uso.
        """

        order.total = self._pricing_strategy.calculate_total(order)

        created_order = self._repository.create_order(order)

        return created_order
