# Instancia principal FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from proyecto_final.api.routers.auth_router import router as auth_router
from proyecto_final.api.routers.health_router import router as health_router
from proyecto_final.api.routers.orders_router import router as orders_router
from proyecto_final.infrastructure.database.models.order_item_model import (  # noqa E402
    OrderItemModel,
)
from proyecto_final.infrastructure.database.models.order_model import (  # noqa E402
    OrderModel,
)
from proyecto_final.infrastructure.database.session import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="APIs Web FastAPI",
    version="1.0.0",
    description="Poyecto final",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro de routers
app.include_router(health_router)
app.include_router(auth_router)
app.include_router(orders_router)
