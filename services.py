import database as database
from db.models import TabletInfo
from typing import  List
from sqlalchemy.orm import Session

def get_all_tablets(session: Session, limit: int, offset: int) -> List[TabletInfo]:
    return session.query(TabletInfo).offset(offset).limit(limit).all()


