from typing import Protocol

from proyecto_final.domain.entities.order import Order


class OrderRepositoryPort(
    Protocol,
):
    """
    Contrato repositorio órdenes.
    """

    def create_order(
        self,
        order: Order,
    ) -> Order:
        """
        Guarda orden.
        """

    def get_orders(
        self,
    ) -> list[Order]:
        """
        Lista órdenes.
        """

    def get_order_by_id(
        self,
        order_id: int,
    ) -> Order | None:
        """
        Busca orden por id.
        """

    def delete_order_by_id(
        self,
        order_id: int,
    ) -> Order | None:
        """
        Borrar orden por id.
        """
