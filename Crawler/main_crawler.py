import API.services as services
import db.models as models
from Crawler.crawl_funcs import Crawl
import time


PATH='https://www.digikala.com/search/category-tablet/?page=1'

class BackgroundTasks():
    
    def run(self):
        try:
            while True:
                self.extract_info()
                print("END!")
                time.sleep(3600)
        except KeyboardInterrupt:
            print('interrupted!')

    def extract_info(self):
        Crawl=Crawl(PATH,diver_path = 'path')
        Crawl.extract_tablet_info()