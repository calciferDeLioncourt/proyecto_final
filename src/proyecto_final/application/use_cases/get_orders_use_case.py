from proyecto_final.domain.entities.order import Order
from proyecto_final.domain.ports.order_repository_port import (
    OrderRepositoryPort,
)
from proyecto_final.domain.pricing.pricing_strategy import PricingStrategy
from proyecto_final.infrastructure.logging.logger import logger


class GetOrdersUseCase:
    """
    Caso de uso para obtener todas las órdenes.
    """

    def __init__(
        self,
        repository: OrderRepositoryPort,
        pricing_strategy: PricingStrategy,
    ) -> None:
        self._repository = repository
        self._pricing_strategy = pricing_strategy

    def execute(self) -> list[Order]:
        """
        Ejecuta el caso de uso para obtener todas las órdenes.

        :return: Lista de órdenes.
        """

        orders = self._repository.get_orders()

        for order in orders:

            order.total = self._pricing_strategy.calculate_total(order)

        logger.info("Obteniendo data")

        return orders
