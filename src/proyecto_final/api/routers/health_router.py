"""
Router health check.
"""

from fastapi import APIRouter

# Router principal
router = APIRouter(
    prefix="",
    tags=["Health"],
)


@router.get(
    "/health",
    summary="Health Check",
)
def health_check() -> dict[str, str]:
    """
    Endpoint de salud.
    """

    return {
        "status": "A la orden para el desorden",
    }
