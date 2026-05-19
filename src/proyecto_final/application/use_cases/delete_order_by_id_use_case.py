from decimal import Decimal

from proyecto_final.domain.entities.order import Order
from proyecto_final.domain.ports.order_repository_port import (
    OrderRepositoryPort,
)
from proyecto_final.infrastructure.logging.logger import logger


class DeleteOrderByIdUseCase:
    """
    Caso de uso para borrar una orden por su ID
    """

    def __init__(
        self,
        repository: OrderRepositoryPort,
    ) -> None:
        self._repository = repository

    def execute(self, order_id: int) -> Order | None:
        """
        Ejecutar caso de uso
        """

        order = self._repository.delete_order_by_id(order_id)

        if order is None:
            return None

        order.total = Decimal("0")

        logger.info("Orden borrada")

        return order
