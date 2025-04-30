from sqlmodel import SQLModel, create_engine, Session
from contextlib import contextmanager
from .config import settings

engine = create_engine(settings.sqlalchemy_uri, echo=False, pool_pre_ping=True)

def init_db() -> None:
    """Run once to create tables."""
    import backend.app.models  # noqa: F401 (imports models for SQLModel metadata)
    SQLModel.metadata.create_all(engine)

@contextmanager
def get_session() -> Session:
    with Session(engine) as session:
        yield session

