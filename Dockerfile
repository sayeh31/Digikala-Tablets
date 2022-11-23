FROM python:3.10.6-bullseye
WORKDIR /code
COPY . .
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install -r requirements.txt
RUN chmod a+x run.sh
EXPOSE 8000
CMD ["./run.sh"]
