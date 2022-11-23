
import pandas as pd
from db.database import engine


class DatabaseFunctions:

    def __init__(self):
        self.engine=engine
        
    def get_ids(self):
        my_data = pd.read_sql("select id from Tablets_Information",self.engine)
        return my_data["id"].values

    def update_Tablet_price(self,id,updated_at, price):

        sql_update_query = """Update Tablets_Information set updated_at=%s, price = %s where id = %s"""
        input_data = (updated_at, price,id)
        self.engine.execute(sql_update_query, input_data)

        print("Record Updated successfully ")

    def insert_varibles_into_table(self,id,created_at,url,price,title,img_url,warranty):

         
         mySql_insert_query = """INSERT INTO Tablets_Information (id,created_at,url,price,title,img_url,warranty) 
                                 VALUES (%s, %s, %s, %s, %s, %s, %s) """

         record = (id,created_at,url,price,title,img_url,warranty)
         self.engine.execute(mySql_insert_query, record)
         print("Record inserted successfully into Tablet_Information table")   
