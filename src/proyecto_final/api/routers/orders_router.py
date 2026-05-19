"""
Router orders.
"""

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.orm import Session

from proyecto_final.api.dependencies.auth_dependency import get_current_user
from proyecto_final.api.dependencies.database_dependency import get_db
from proyecto_final.api.schemas.order_request import OrderCreateSchema
from proyecto_final.api.schemas.order_response import (
    OrderItemResponseSchema,
    OrderResponseSchema,
)
from proyecto_final.application.use_cases.create_order_use_case import (
    CreateOrderUseCase,
)
from proyecto_final.application.use_cases.delete_order_by_id_use_case import (
    DeleteOrderByIdUseCase,
)
from proyecto_final.application.use_cases.get_order_by_id_use_case import (
    GetOrderByIdUseCase,
)
from proyecto_final.application.use_cases.get_orders_use_case import (
    GetOrdersUseCase,
)
from proyecto_final.domain.entities.order import Order
from proyecto_final.domain.entities.order_item import OrderItem
from proyecto_final.domain.enums.pricing_strategy_type import (
    PricingStrategyType,
)
from proyecto_final.domain.factories.pricing_strategy_factory import (
    PricingStrategyFactory,
)
from proyecto_final.infrastructure.notifications.notification_dispatcher import (
    NotificationDispatcher,
)
from proyecto_final.infrastructure.repositories.sqlalchemy_order_repository import (
    SQLAlchemyOrderRepository,
)

# Router principal
router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


@router.post(
    "",
    summary="Create Order",
    response_model=OrderResponseSchema,
)
async def create_order_endpoint(
    background_tasks: BackgroundTasks,
    schema: OrderCreateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
) -> OrderResponseSchema:
    """
    Endpoint to create a new order.
    """
    repository = SQLAlchemyOrderRepository(db)
    pricing_strategy = PricingStrategyFactory.create(
        PricingStrategyType.REGULAR
    )

    use_case = CreateOrderUseCase(
        repository=repository,
        pricing_strategy=pricing_strategy,
    )

    order = Order(
        customer_name=(schema.customer_name),
        items=[
            OrderItem(
                product_name=item.product_name,
                quantity=item.quantity,
                price=item.price,
            )
            for item in schema.items
        ],
    )

    result = use_case.execute(order=order)

    dispatcher = NotificationDispatcher()

    background_tasks.add_task(
        dispatcher.send_notifications,
        [result],
    )

    assert result.id is not None

    items = []

    for item in result.items:
        assert item.id is not None
        items.append(
            OrderItemResponseSchema(
                id=item.id,
                product_name=(item.product_name),
                quantity=item.quantity,
                price=item.price,
            )
        )

    return OrderResponseSchema(
        id=result.id,
        customer_name=result.customer_name,
        items=items,
        total=result.total,
    )


@router.get(
    "/{strategy}",
    summary="Get All Orders",
    response_model=list[OrderResponseSchema],
)
def get_orders_endpoint(
    strategy: PricingStrategyType,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
) -> list[OrderResponseSchema]:
    """
    Endpoint to get all orders.
    """

    repository = SQLAlchemyOrderRepository(db)
    pricing_strategy = PricingStrategyFactory.create(strategy)

    use_case = GetOrdersUseCase(
        repository=repository, pricing_strategy=pricing_strategy
    )

    result = use_case.execute()

    orders = []

    for order in result:
        assert order.id is not None
        items = []

        for item in order.items:
            assert item.id is not None
            items.append(
                OrderItemResponseSchema(
                    id=item.id,
                    product_name=(item.product_name),
                    quantity=item.quantity,
                    price=item.price,
                )
            )

        orders.append(
            OrderResponseSchema(
                id=order.id,
                customer_name=order.customer_name,
                items=items,
                total=order.total,
            )
        )

    return orders


@router.get(
    "/{order_id}/{strategy}",
    summary="Get Order by ID",
    response_model=OrderResponseSchema,
)
def get_order_by_id_endpoint(
    order_id: int,
    strategy: PricingStrategyType,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
) -> OrderResponseSchema:
    """
    Endpoint to get order by ID.
    """
    pricing_strategy = PricingStrategyFactory.create(strategy)

    repository = SQLAlchemyOrderRepository(db)

    use_case = GetOrderByIdUseCase(
        repository=repository, pricing_strategy=pricing_strategy
    )

    order = use_case.execute(order_id=order_id)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    assert order.id is not None

    items = []

    for item in order.items:
        assert item.id is not None
        items.append(
            OrderItemResponseSchema(
                id=item.id,
                product_name=(item.product_name),
                quantity=item.quantity,
                price=item.price,
            )
        )

    return OrderResponseSchema(
        id=order.id,
        customer_name=order.customer_name,
        items=items,
        total=order.total,
    )


@router.delete(
    "/{order_id}",
    summary="Delete Order by ID",
    response_model=OrderResponseSchema,
)
def delete_order_by_id_endpoint(
    order_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
) -> OrderResponseSchema:
    """
    Endpoint to delete order by ID.
    """
    repository = SQLAlchemyOrderRepository(db)

    use_case = DeleteOrderByIdUseCase(
        repository=repository,
    )

    order = use_case.execute(order_id=order_id)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    assert order.id is not None

    items = []

    for item in order.items:
        assert item.id is not None
        items.append(
            OrderItemResponseSchema(
                id=item.id,
                product_name=(item.product_name),
                quantity=item.quantity,
                price=item.price,
            )
        )

    return OrderResponseSchema(
        id=order.id,
        customer_name=order.customer_name,
        items=items,
        total=order.total,
    )
