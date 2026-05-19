# Instancia principal FastAPI
from fastapi import FastAPI

from proyecto_final.api.routers.auth_router import router as auth_router
from proyecto_final.api.routers.health_router import (
    router as health_router,
)
from proyecto_final.api.routers.orders_router import (
    router as orders_router,
)

app = FastAPI(
    title="APIs Web FastAPI",
    version="1.0.0",
    description="Test Intermediate Level API",
)

# Registro de routers
app.include_router(health_router)
app.include_router(auth_router)
app.include_router(orders_router)
