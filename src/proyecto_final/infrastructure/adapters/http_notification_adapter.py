from proyecto_final.domain.entities.order import Order
from proyecto_final.infrastructure.logging.logger import logger


class HttpNotificationAdapter:
    """
    Simulate external HTTP provider.
    """

    def send_order_created(
        self,
        order: Order,
    ) -> None:

        logger.info(
            f"""
            Sending notification
            for order {order.id}
            """
        )
