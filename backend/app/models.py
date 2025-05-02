from typing import Optional
from datetime import date, time
from sqlmodel import SQLModel, Field

class Game(SQLModel, table=True):
    __tablename__ = "games"          # existing MySQL table

    game_id: Optional[int] = Field(primary_key=True)
    game_date: date
    start_time_local: Optional[time] = None
    start_time_et: Optional[time] = None
    home_team_id: int
    away_team_id: int
