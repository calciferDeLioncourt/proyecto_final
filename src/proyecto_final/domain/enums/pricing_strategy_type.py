from enum import Enum


class PricingStrategyType(
    str,
    Enum,
):

    REGULAR = "regular"

    VIP = "vip"

    EMPLOYEE = "employee"

    BLACK_FRIDAY = "black_friday"
