#!/bin/bash

if  [[ ! -f "/opt/airflow/airflow.db" ]]
then
    airflow db init;
	airflow users create --username admin --firstname admin --lastname admin --role Admin --email admin@admin.org --password admin;
fi;

airflow scheduler & airflow webserver -p 3000;