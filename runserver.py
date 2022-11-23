import uvicorn
from API.main_API import app

app.debug =True
if __name__ =='__main__':

    uvicorn.run('runserver:app',host='127.0.0.1',port=8000,reload=True)