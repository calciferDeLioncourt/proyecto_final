from sqlalchemy.orm import Session

from proyecto_final.domain.entities.order import Order
from proyecto_final.domain.entities.order_item import OrderItem
from proyecto_final.domain.ports.order_repository_port import (
    OrderRepositoryPort,
)
from proyecto_final.infrastructure.database.models.order_item_model import (
    OrderItemModel,
)
from proyecto_final.infrastructure.database.models.order_model import (
    OrderModel,
)
from proyecto_final.infrastructure.logging.logger import logger


class SQLAlchemyOrderRepository(OrderRepositoryPort):
    """
    Repository SQLAlchemy.
    """

    def __init__(
        self,
        db: Session,
    ) -> None:

        self._db = db

    def create_order(
        self,
        order: Order,
    ) -> Order:
        """
        Persiste orden.
        """

        db_order = OrderModel(
            customer_name=(order.customer_name),
            items=[
                OrderItemModel(
                    product_name=item.product_name,
                    quantity=item.quantity,
                    price=item.price,
                )
                for item in order.items
            ],
        )

        self._db.add(
            db_order,
        )

        self._db.commit()

        self._db.refresh(
            db_order,
        )

        return Order(
            id=db_order.id,
            customer_name=(db_order.customer_name),
            items=[
                OrderItem(
                    id=item.id,
                    product_name=item.product_name,
                    quantity=item.quantity,
                    price=item.price,
                )
                for item in db_order.items
            ],
            total=order.total,
        )

    def get_orders(
        self,
    ) -> list[Order]:
        """
        Obtiene todas las órdenes.
        """

        db_orders = self._db.query(OrderModel).all()

        return [
            Order(
                id=db_order.id,
                customer_name=(db_order.customer_name),
                items=[
                    OrderItem(
                        id=item.id,
                        product_name=item.product_name,
                        quantity=item.quantity,
                        price=item.price,
                    )
                    for item in db_order.items
                ],
            )
            for db_order in db_orders
        ]

    def get_order_by_id(
        self,
        order_id: int,
    ) -> Order | None:
        """
        Obtiene orden por id.
        """

        db_order = (
            self._db.query(OrderModel)
            .filter(OrderModel.id == order_id)
            .first()
        )

        if not db_order:
            return None

        return Order(
            id=db_order.id,
            customer_name=(db_order.customer_name),
            items=[
                OrderItem(
                    id=item.id,
                    product_name=item.product_name,
                    quantity=item.quantity,
                    price=item.price,
                )
                for item in db_order.items
            ],
        )

    def delete_order_by_id(
        self,
        order_id: int,
    ) -> Order | None:
        """
        Obtiene orden por id.
        """

        db_order = (
            self._db.query(OrderModel)
            .filter(OrderModel.id == order_id)
            .first()
        )

        if not db_order:
            return None

        self._db.delete(db_order)

        self._db.commit()

        logger.info(
            "Orden eliminada",
        )
        return Order(
            id=db_order.id,
            customer_name=(db_order.customer_name),
            items=[
                OrderItem(
                    id=item.id,
                    product_name=item.product_name,
                    quantity=item.quantity,
                    price=item.price,
                )
                for item in db_order.items
            ],
        )
