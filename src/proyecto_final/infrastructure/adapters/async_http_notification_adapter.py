import asyncio

from proyecto_final.domain.entities.order import Order
from proyecto_final.infrastructure.logging.logger import logger


class AsyncHttpNotificationAdapter:
    """
    Async notification adapter.
    """

    async def send_order_created(
        self,
        order: Order,
    ) -> None:

        await asyncio.sleep(1)

        logger.info(
            f"""
            Async notification
            sent for order {order.id}
            """
        )
