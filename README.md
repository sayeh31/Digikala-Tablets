<h1>Digikala Crawler</h1>
<h2></h2>

You can read this document to get a basic grasp on how to run this project , it's services and what they do and general information about how to start project as someone who is new to Python.
<h1>Runnig with Docker</h1>



<h1>Running without Docker</h1>

step1: please replace your MySql connection information in 
```config/cfg.py```

step2: install requirements.txt  
```pip install -r requirements.txt```

step3: create tablet information tabel in mysql db using 
```python tablet_initial.py```

step4: extract tablets information from digikala and insert/updated db using 
```python startup.py```

step5: create api to get tablets information using 
```python runserver.py```

