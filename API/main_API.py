import fastapi as fastapi
import API.services as services
import db.models as models
from fastapi import  Depends
from sqlalchemy.orm import Session
from API.services import get_all_tablets
from db.database import  SessionLocal, engine
from API.schemas import PaginatedTabletInfo


# region API

app= fastapi.FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/Tablets", response_model=PaginatedTabletInfo)
def list_Tablets(session: Session = Depends(get_db), limit: int = 10, offset: int = 0):
     tablets_list = get_all_tablets(session, limit, offset)
     response = {"limit": limit, "offset": offset, "data": tablets_list}
     return response


# endregion

