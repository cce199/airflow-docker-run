import airflow
from airflow.models import DAG
from airflow import configuration

from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

import pendulum
import datetime
import os
from datetime import datetime, timedelta

local_tz = pendulum.timezone("Asia/Seoul")

default_args = {
    'owner': 'data',
    'depends_on_past': True,
    #'start_date': airflow.utils.dates.days_ago(1), #datetime(2019, 4, 23, tzinfo= local_tz),
    'start_date': local_tz.convert(airflow.utils.dates.days_ago(2)),
    'email': ['root@email.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 60,
    'retry_delay': timedelta(minutes=2),
    # 'on_failure_callback': task_fail_slack_alert,
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG(
    dag_id='TaskAirflow1',
    default_args=default_args,
    schedule_interval='5 0 * * *', #timedelta(days=1),
    max_active_runs=1
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)

sleep1 = BashOperator(
    task_id='sleep1',
    bash_command='sleep 120',
    dag=dag)

tDone = BashOperator(
    task_id='done',
    bash_command='echo "done"',
    dag=dag)

t1 >> sleep1 >> tDone
