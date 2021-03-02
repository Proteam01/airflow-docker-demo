from airflow.models import DAG
from datetime import datetime
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner':'Carlos',
    'start_date': datetime(2021,1,1) 
}

def perform_method():
    print('executing test dag.')


with DAG('test_carlos_dag',
          default_args=default_args, 
          schedule_interval='@daily',
          catchup=False) as dag:
    start = DummyOperator(task_id='start')
    perform = PythonOperator(task_id='perform',python_callable=perform_method)
    end = DummyOperator(task_id='end')

start >> perform >> end
