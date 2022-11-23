import datetime as dt
from typing import Optional, List
from pydantic import BaseModel

class Tablet(BaseModel):
    id:int
    created_at: dt.datetime
    updated_at: Optional[dt.datetime] = None
    url:str
    title: str
    price:int
    img_url:str
    warranty: str

    class Config:
        orm_mode = True

class PaginatedTabletInfo(BaseModel):
    limit: int
    offset: int
    data: List[Tablet]        

