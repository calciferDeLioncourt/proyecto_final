from proyecto_final.domain.entities.order import Order
from proyecto_final.domain.ports.order_repository_port import (
    OrderRepositoryPort,
)
from proyecto_final.domain.pricing.pricing_strategy import (
    PricingStrategy,
)


class GetOrderByIdUseCase:
    """
    Caso de uso para obtener una orden por su ID.
    """

    def __init__(
        self,
        repository: OrderRepositoryPort,
        pricing_strategy: PricingStrategy,
    ) -> None:
        self._repository = repository
        self._pricing_strategy = pricing_strategy

    def execute(self, order_id: int) -> Order | None:
        """
        Ejecuta el caso de uso.

        Args:
            order_id (int): ID de la orden a obtener.

        Returns:
            Order | None: La orden obtenida o None si no se encuentra.
        """

        order = self._repository.get_order_by_id(order_id)
        if order is None:
            return None

        order.total = self._pricing_strategy.calculate_total(order)
        return order
