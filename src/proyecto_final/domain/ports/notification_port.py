from typing import Protocol

from proyecto_final.domain.entities.order import Order


class NotificationPort(
    Protocol,
):

    def send_order_created(
        self,
        order: Order,
    ) -> None: ...
