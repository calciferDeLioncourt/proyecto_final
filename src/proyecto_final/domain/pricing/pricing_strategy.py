from decimal import Decimal
from typing import Protocol

from proyecto_final.domain.entities.order import Order


class PricingStrategy(
    Protocol,
):
    """
    Contrato PricingStrategy
    """

    def calculate_total(
        self,
        order: Order,
    ) -> Decimal: ...
