from decimal import Decimal

from proyecto_final.domain.entities.order import Order
from proyecto_final.infrastructure.logging.logger import logger


class VipPricingStrategy:

    def calculate_total(
        self,
        order: Order,
    ) -> Decimal:

        subTotal = sum(item.price * item.quantity for item in order.items)

        tax = (subTotal * Decimal("0.16")).quantize(Decimal("0.01"))
        logger.info(f"I.V.A {tax}")

        logger.info("--------")
        logger.info(f"subTotal {subTotal}")
        logger.info("--------")

        total = subTotal + tax
        logger.info(f"Total {total}")

        return total * Decimal("0.80")
