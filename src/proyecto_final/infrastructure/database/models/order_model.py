from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from proyecto_final.infrastructure.database.base import Base

if TYPE_CHECKING:
    from proyecto_final.infrastructure.database.models.order_item_model import (
        OrderItemModel,
    )


class OrderModel(Base):
    """
    Entidad orden.
    """

    __tablename__ = "orders"

    # Primary key
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    # Nombre cliente
    customer_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    # Relación items
    items: Mapped[list["OrderItemModel"]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan",
    )
