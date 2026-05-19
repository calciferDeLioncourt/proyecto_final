import asyncio
import time

from proyecto_final.domain.entities.order import Order
from proyecto_final.infrastructure.logging.logger import logger
from proyecto_final.infrastructure.notifications.notification_dispatcher import (
    NotificationDispatcher,
)


async def main():

    dispatcher = NotificationDispatcher()

    orders = [
        Order(
            id=i,
            customer_name="Alberto",
            items=[],
        )
        for i in range(10)
    ]

    start = time.perf_counter()

    await dispatcher.send_notifications(orders)

    end = time.perf_counter()

    logger.info(
        f"""
        Total time:
        {end - start:.2f}
        seconds
        """
    )


asyncio.run(main())
