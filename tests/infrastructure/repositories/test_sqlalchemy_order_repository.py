from decimal import Decimal

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from proyecto_final.domain.entities.order import Order
from proyecto_final.domain.entities.order_item import OrderItem
from proyecto_final.infrastructure.database.base import Base
from proyecto_final.infrastructure.repositories.sqlalchemy_order_repository import (
    SQLAlchemyOrderRepository,
)

engine = create_engine("sqlite:///:memory:")

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base.metadata.create_all(
    bind=engine,
)


def get_repository():

    Base.metadata.drop_all(
        bind=engine,
    )

    Base.metadata.create_all(
        bind=engine,
    )

    db = TestingSessionLocal()

    return (
        SQLAlchemyOrderRepository(db),
        db,
    )


def test_should_create_order():

    repository, db = get_repository()

    order = Order(
        customer_name="Alberto",
        items=[
            OrderItem(
                product_name="Keyboard",
                quantity=2,
                price=Decimal("1000.00"),
            )
        ],
    )

    result = repository.create_order(
        order,
    )

    assert result.id is not None

    assert result.customer_name == "Alberto"

    assert len(result.items) == 1

    assert result.items[0].product_name == "Keyboard"

    db.close()


def test_should_get_orders():

    repository, db = get_repository()

    order = Order(
        customer_name="Alberto",
        items=[
            OrderItem(
                product_name="Keyboard",
                quantity=1,
                price=Decimal("500.00"),
            )
        ],
    )

    repository.create_order(
        order,
    )

    result = repository.get_orders()

    assert len(result) == 1

    assert result[0].customer_name == "Alberto"

    db.close()


def test_should_get_order_by_id():

    repository, db = get_repository()

    created_order = repository.create_order(
        Order(
            customer_name="Alberto",
            items=[
                OrderItem(
                    product_name="Keyboard",
                    quantity=1,
                    price=Decimal("500.00"),
                )
            ],
        )
    )

    result = repository.get_order_by_id(created_order.id)

    assert result is not None

    assert result.id == created_order.id

    assert result.customer_name == "Alberto"

    db.close()
