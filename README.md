# Digikala Crawler
Digikala Crawler is a Selenium-based web crawler with an accompanying REST API that will scrape the info of the top tablets currently being sold in Digikala and store them in a database that can be accessed via the accompanying REST API.

# Table of contents
- [1. Minimum requirements to run the project](#1-minimum-requirements-to-run-the-project)
- [2. Running the project](#2-running-the-project)
  - [2.1. Running the project using Docker](#21-running-the-project-using-docker)
  - [2.2. Running the project manually](#22-running-the-project-manually)
  - [2.3. Contributions](#23-contributions)

# 1. Minimum requirements to run the project
- Python 3.7
- MySQL/MariaDB
- Docker (if you want to run using Docker)

# 2. Running the project
There are two ways to run the project:
- Running using Docker
- Running manually

## 2.1. Running the project using Docker
 1. Clone the project:
    ```console
    $ git clone https://github.com/sayeh31/Digikala-Tablets.git
    ```

 2. Add your environment settings (Database address, credentials and name) to the `.env` file.

 3. Run the following command to get the project up and running:
    ```console
     $ sudo docker run -d -p 8000:8000 -e .env sayeh:latest
    ```


## 2.2. Running the project manually
1. Make sure you have `python3` installed on your system.

2. Set up your database environment settings by modifying the following variables inside `config/cfg.py`:
   ```python
   # database address
   DEFAULT_HOST= "127.0.0.1"
   # database username
   DEFAULT_ROOT= "root"
   # database password
   DEFAULT_PASS= "123456"
   # name of the database you want the tables to be stored in
   DEFAULT_DATABASE= "digikala"
   ```
3. Install the required libraries to run the project:
    ```console
    $ pip install -r requirements.txt
    ```

4. Run the table creation script to create the necessary MySQL tables for the project:
    ```console
    $ python tablet_initial.py
    ```

5. Run the scraper to feed data into the database:
    ```console
    $ python python startup.py
    ```
    The scraper is responsible for adding/updating data to the database, so if it's not running, no new data will be added or updated.

6. Run the REST API server:
    ```console
    $ python runserver.py
    ```
    The API can be accessed at `http://localhost:8000`.‌ This API is responsible for reading all the data gathered by the scraper from the database.

## 2.3. Contributions
This project is far from perfect and all PRs and other contributions are most welcome :)

