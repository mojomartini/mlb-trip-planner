from typing import Optional
from datetime import date, time, datetime
from sqlmodel import SQLModel, Field, Column, DateTime

class Game(SQLModel, table=True):
    __tablename__ = "games"

    game_id: Optional[int] = Field(primary_key=True)
    game_date: date
    start_time_local: Optional[time] = None
    start_time_et: Optional[time] = None
    home_team_id: int
    away_team_id: int

    # existing nullable column in your table
    date_utc: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), nullable=True)
    )
