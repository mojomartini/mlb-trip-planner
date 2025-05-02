from fastapi import APIRouter, Depends, Query
from typing import List
from datetime import date
from sqlmodel import select
from backend.app.core.database import get_session
from backend.app.models import Game

router = APIRouter(prefix="/games", tags=["Games"])

@router.get("/", response_model=List[Game])
def list_games(
    date_from: date = Query(..., description="YYYY-MM-DD"),
    date_to: date = Query(..., description="YYYY-MM-DD"),
    session = Depends(get_session),
):
    stmt = (
        select(Game)
        .where(Game.game_date >= date_from)
        .where(Game.game_date <= date_to)
        .order_by(Game.game_date)
    )
    return session.exec(stmt).all()
