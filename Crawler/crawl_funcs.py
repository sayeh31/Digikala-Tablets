import pandas as pd
from Crawler.selenium_funcs import SeleniumFunctions
from Crawler.database_funcs import DatabaseFunctions
import time
import warnings
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from webdriver_manager import chrome
from config.cfg import driver



class Crawl:
    
    def __init__(self,path,diver_path = None):
        self.path=path
        self.diver_path = driver["diver_path"]

    def extract_tablet_info(self):
        warnings.filterwarnings('ignore')
        if self.diver_path is None:
            self.diver_path = chrome.ChromeDriverManager().install()
        seleniumfunctions=SeleniumFunctions(self.diver_path)
        databasefunctions=DatabaseFunctions()

        products=seleniumfunctions.get_products_list(self.path)
        
        existing_products=databasefunctions.get_ids()
        for product in products:
            seleniumfunctions.get_product_page(product)
            time.sleep(10)
            id= int(product.split("/")[4].split("-")[1])
            if not id in existing_products:
                new_tablet_data=seleniumfunctions.new_tablet_info(product)
                id,created_at,url,price,title,img_url,warranty=new_tablet_data
                databasefunctions.insert_varibles_into_table(id,created_at,url,price,title,img_url,warranty)
            else:
                updated_tablet_data =seleniumfunctions.updated_tablet(product)
                id,updated_at,price=updated_tablet_data
                databasefunctions.update_Tablet_price(id,updated_at,price)
        seleniumfunctions.close()        