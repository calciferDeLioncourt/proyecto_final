"""
Dependencias relacionadas con base de datos.
"""

from collections.abc import Generator

from sqlalchemy.orm import Session

from proyecto_final.infrastructure.database.session import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """
    Proporciona sesión DB.
    """

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()
