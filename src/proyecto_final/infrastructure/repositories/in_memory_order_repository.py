from proyecto_final.domain.entities.order import Order
from proyecto_final.domain.ports.order_repository_port import (
    OrderRepositoryPort,
)


class InMemoryOrderRepository(OrderRepositoryPort):
    """
    In-memory repository adapter.
    """

    def __init__(self):

        self._orders: list[Order] = []

        self._id_counter = 1

    def create_order(
        self,
        order: Order,
    ) -> Order:

        order.id = self._id_counter

        self._id_counter += 1

        self._orders.append(order)

        return order

    def get_orders(
        self,
    ) -> list[Order]:

        return self._orders

    def get_order_by_id(
        self,
        order_id: int,
    ) -> Order | None:

        for order in self._orders:

            if order.id == order_id:

                return order

        return None
