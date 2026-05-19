import asyncio

from proyecto_final.domain.entities.order import Order
from proyecto_final.infrastructure.adapters.async_http_notification_adapter import (
    AsyncHttpNotificationAdapter,
)


class NotificationDispatcher:
    """
    Async concurrent dispatcher.
    """

    def __init__(
        self,
        max_concurrent: int = 3,
    ):

        self._semaphore = asyncio.Semaphore(max_concurrent)

        self._adapter = AsyncHttpNotificationAdapter()

    async def _send(
        self,
        order: Order,
    ) -> None:

        async with self._semaphore:

            await self._adapter.send_order_created(order)

    async def send_notifications(
        self,
        orders: list[Order],
    ) -> None:

        tasks = [self._send(order) for order in orders]

        await asyncio.gather(*tasks)
