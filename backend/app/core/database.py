"""
Database engine and session helper
"""

from sqlmodel import SQLModel, create_engine, Session
from backend.app.core.config import settings

# ── 1. Engine ---------------------------------------------------
engine = create_engine(
    settings.sqlalchemy_uri,
    echo=False,
    pool_pre_ping=True,
)

# ── 2. Session dependency for FastAPI ---------------------------
def get_session():
    """
    FastAPI dependency.
    Yields an active Session object and closes it after the request.
    Usage:

        from fastapi import Depends
        @router.get("/")
        def endpoint(session: Session = Depends(get_session)):
            ...
    """
    with Session(engine) as session:
        yield session
