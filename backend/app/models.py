from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class Game(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date_utc: datetime
    home_team: str
    away_team: str
    stadium: str
    tz: str
    first_pitch_local: datetime

