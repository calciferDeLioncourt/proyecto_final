from decimal import Decimal

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from proyecto_final.domain.entities.order import Order
from proyecto_final.domain.entities.order_item import OrderItem
from proyecto_final.infrastructure.database.base import Base
from proyecto_final.infrastructure.repositories.in_memory_order_repository import (
    InMemoryOrderRepository,
)
from proyecto_final.infrastructure.repositories.sqlalchemy_order_repository import (
    SQLAlchemyOrderRepository,
)


def create_sqlalchemy_repository():

    engine = create_engine("sqlite:///:memory:")

    TestingSessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )

    Base.metadata.create_all(
        bind=engine,
    )

    db = TestingSessionLocal()

    repository = SQLAlchemyOrderRepository(db)

    return (repository, db)


@pytest.fixture(
    params=[
        "memory",
        "sqlalchemy",
    ]
)
def repository(request):

    if request.param == "memory":

        yield (InMemoryOrderRepository())

    elif request.param == "sqlalchemy":

        repository, db = create_sqlalchemy_repository()

        yield repository

        db.close()


def test_should_create_order(
    repository,
):
    """
    All repositories
    should create orders.
    """

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

    result = repository.create_order(order)

    assert result.id is not None

    assert result.customer_name == "Alberto"


def test_should_get_orders(
    repository,
):
    """
    All repositories
    should return orders.
    """

    repository.create_order(
        Order(
            customer_name="Alberto",
            items=[
                OrderItem(
                    product_name="Mouse",
                    quantity=1,
                    price=Decimal("500.00"),
                )
            ],
        )
    )

    result = repository.get_orders()

    assert len(result) == 1


def test_should_get_order_by_id(
    repository,
):
    """
    All repositories
    should retrieve order by id.
    """

    created_order = repository.create_order(
        Order(
            customer_name="Alberto",
            items=[
                OrderItem(
                    product_name="Monitor",
                    quantity=1,
                    price=Decimal("2000.00"),
                )
            ],
        )
    )

    result = repository.get_order_by_id(created_order.id)

    assert result is not None

    assert result.id == created_order.id
