
import API.services as services
import db.models as models
from Curller.Curl_funcs import Curl
import time
import threading



PATH='https://www.digikala.com/search/category-tablet/?page=1'

class BackgroundTasks(threading.Thread):
    
    def run(self):
        try:
            while True:
                self.extract_info()
                print("END!")
                time.sleep(3600)
        except KeyboardInterrupt:
            print('interrupted!')

    def extract_info(self):
        curl=Curl(PATH)
        curl.extract_tablet_info()