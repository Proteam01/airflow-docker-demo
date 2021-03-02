FROM python:3.9

WORKDIR /opt/airflow

RUN export AIRFLOW_HOME=/opt/airflow

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./airflow.cfg .

EXPOSE 3000

