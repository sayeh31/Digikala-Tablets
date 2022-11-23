from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time


class SeleniumFunctions:

    def __init__(self,chorome_path):
        self.chorome_path=chorome_path
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        self.driver = webdriver.Chrome(options=self.chrome_options,executable_path=chorome_path)

        #self.driver = webdriver.Chrome("chromedriver.exe" )    
        
    def get_product_page(self,path):
        self.driver.get(path)
    
    def close(self):
        self.driver.close()
    
    def get_products_list(self,path):
        self.driver.get(path)
        time.sleep(10)
        page1=self.driver.find_element(by=By.XPATH,value="//section[1]/div[2]")
        products=list(map(lambda x:x.get_attribute("href"),page1.find_elements(by=By.TAG_NAME,value="a")))
        return products    

    def new_tablet_info(self,product):
        id= int(product.split("/")[4].split("-")[1])
        tb_img=self.driver.find_element(by=By.XPATH,value="//div[contains(@class,'ProductContent')]//div[contains(@class,'InfoSection')]//div[contains(@class,'pos-relative')]//div[contains(@class,'swiper-container')]//div[contains(@class,'swiper-slide')][1]//img")
        img_link=tb_img.get_attribute("src")
        name=tb_img.get_attribute("alt")
        warranty=self.driver.find_element(by=By.XPATH, value="//div[1]/div[2]/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div[4]/div/div[2]/p").text
        price=self.driver.find_element(by=By.XPATH, value="//div/div/div[1]/div[2]/div[2]/div[1]/span").text
        created_at=datetime.now()
        return id,created_at,product,int(price.replace(",","")),name,img_link,warranty

    def updated_tablet(self,product):
        id=int(product.split("/")[4].split("-")[1])
        price=self.driver.find_element(by=By.XPATH, value="//div/div/div[1]/div[2]/div[2]/div[1]/span").text
        updated_at=datetime.now()
        return id,updated_at,int(price.replace(",",""))
