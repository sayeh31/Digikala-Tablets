import sqlalchemy.orm as orm
import sqlalchemy as sql
from db.database import base


class TabletInfo(base):
    __tablename__="Tablets_Information"
    id= sql.Column(sql.Integer,primary_key=True)
    created_at= sql.Column(sql.DateTime)
    updated_at= sql.Column(sql.DateTime)
    url= sql.Column(sql.String(1000))
    title= sql.Column(sql.String(200))
    price=sql.Column(sql.Integer)
    img_url= sql.Column(sql.String(500))
    warranty= sql.Column(sql.String(200))


