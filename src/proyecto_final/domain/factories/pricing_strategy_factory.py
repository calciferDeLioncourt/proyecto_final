from proyecto_final.domain.enums.pricing_strategy_type import (
    PricingStrategyType,
)
from proyecto_final.domain.pricing.black_friday_strategy import (
    BlackFridayPricingStrategy,
)
from proyecto_final.domain.pricing.cached_pricing_strategy import (
    CachedPricingStrategy,
)
from proyecto_final.domain.pricing.employee_pricing_strategy import (
    EmployeePricingStrategy,
)
from proyecto_final.domain.pricing.regular_pricing_strategy import (
    RegularPricingStrategy,
)
from proyecto_final.domain.pricing.vip_pricing_strategy import (
    VipPricingStrategy,
)


class PricingStrategyFactory:

    @staticmethod
    def create(
        strategy_type: PricingStrategyType,
    ):

        if strategy_type == PricingStrategyType.REGULAR:
            return CachedPricingStrategy(RegularPricingStrategy())

        if strategy_type == PricingStrategyType.VIP:
            return CachedPricingStrategy(VipPricingStrategy())

        if strategy_type == PricingStrategyType.EMPLOYEE:
            return CachedPricingStrategy(EmployeePricingStrategy())

        if strategy_type == PricingStrategyType.BLACK_FRIDAY:
            return CachedPricingStrategy(BlackFridayPricingStrategy())

        raise ValueError("Invalid pricing strategy")
