FROM python:3.10.6-bullseye
WORKDIR /opt
COPY . .
RUN pip install -r requirements.txt 
RUN chmod a+x run.sh
EXPOSE 8000
CMD ["./run.sh"]