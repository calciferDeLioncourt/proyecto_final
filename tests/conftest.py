import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from proyecto_final.api.dependencies.database_dependency import get_db
from proyecto_final.api.main import app
from proyecto_final.infrastructure.database.base import Base

TEST_DATABASE_URL = "sqlite:///./data/test_orders.db"

test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine,
)


def override_get_db():

    db = TestingSessionLocal()

    try:

        yield db

    finally:

        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def setup_database():

    Base.metadata.create_all(
        bind=test_engine,
    )

    yield

    Base.metadata.drop_all(
        bind=test_engine,
    )
