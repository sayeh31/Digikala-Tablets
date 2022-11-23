
#Database Configs
import os


DEFAULT_HOST= "127.0.0.1",
DEFAULT_ROOT= "root",
DEFAULT_PASS= "123456",
DEFAULT_DATABASE= "digikala",

driver={"diver_path": None}


mysql = {
    "host":  os.environ.get("HOST", DEFAULT_HOST),
    "user":os.environ.get("ROOT", DEFAULT_ROOT) ,
    "passwd": os.environ.get("PASS", DEFAULT_PASS),
    "db": os.environ.get("DATABASE", DEFAULT_DATABASE),
}
