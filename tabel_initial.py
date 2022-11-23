from db.database import engine
import db.models as models
import sqlalchemy as sa
import config.cfg as cfg

def check_table(engine):
    insp = sa.inspect(engine)
    if not insp.has_table("Tablets_Information", schema=cfg.mysql["db"]):  
        models.base.metadata.create_all(bind=engine)
        return print("Tablets_Information Table Created!")
    else: return print("Tablets_Information Table already exists!")                
                
if __name__ =='__main__':
    check_table(engine)