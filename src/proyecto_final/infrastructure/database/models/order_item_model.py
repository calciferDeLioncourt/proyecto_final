from __future__ import annotations

from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from proyecto_final.infrastructure.database.base import Base

if TYPE_CHECKING:
    from proyecto_final.infrastructure.database.models.order_model import (
        OrderModel,
    )


class OrderItemModel(Base):
    """
    Entidad item de orden.
    """

    __tablename__ = "order_items"

    # Primary key
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    # Nombre producto
    product_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    # Cantidad
    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    # Precio
    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    # Foreign key
    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id"),
    )

    # Relación orden
    order: Mapped["OrderModel"] = relationship(
        back_populates="items",
    )
