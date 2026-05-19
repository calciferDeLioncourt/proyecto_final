from decimal import Decimal

from proyecto_final.domain.entities.order import Order
from proyecto_final.domain.pricing.pricing_strategy import (
    PricingStrategy,
)


class CachedPricingStrategy:
    """
    Decorator strategy with cache.
    """

    def __init__(
        self,
        strategy: PricingStrategy,
    ):

        self._strategy = strategy

        self._cache: dict[
            int,
            Decimal,
        ] = {}

    def calculate_total(
        self,
        order: Order,
    ) -> Decimal:

        if order.id is None:

            return self._strategy.calculate_total(order)

        if order.id in self._cache:

            return self._cache[order.id]

        total = self._strategy.calculate_total(order)

        self._cache[order.id] = total

        return total
