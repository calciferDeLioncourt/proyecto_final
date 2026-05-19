from proyecto_final.infrastructure.database.base import Base

# IMPORTANTE
# cargar models
from proyecto_final.infrastructure.database.models import (  # noqa: F401
    OrderItemModel,
    OrderModel,
)
from proyecto_final.infrastructure.database.session import engine

print(
    "Creating database...",
)

Base.metadata.create_all(
    bind=engine,
)

print(
    "Database created successfully.",
)
