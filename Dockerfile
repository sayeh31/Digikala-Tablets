FROM python:3.10.6-bullseye
WORKDIR /opt
COPY ./requirements.txt /opt
RUN pip install --no-cache-dir --upgrade -r /opt/requirements.txt
COPY . . 
RUN chmod a+x run.sh
EXPOSE 8000
CMD ["./run.sh"]