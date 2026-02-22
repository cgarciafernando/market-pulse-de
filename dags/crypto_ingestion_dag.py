from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'engineer',
    'depends_on_past': False,
    'start_date': datetime(2026, 2, 22),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'market_pulse_ingestion',
    default_args=default_args,
    description='Crypto ETL pipeline',
    schedule_interval='@hourly',
    catchup=False
) as dag:

    task_check_api = BashOperator(
        task_id='check_api_status',
        bash_command='curl -I https://api.coingecko.com/api/v3/ping'
    )

    task_run_ingestor = BashOperator(
        task_id='run_docker_ingestor',
        bash_command='python3 /opt/airflow/scripts/api_to_db.py'
    )

    task_transform = BashOperator(
        task_id='transform_data',
        bash_command='python3 /opt/airflow/scripts/transform_data.py'
    )

    task_check_api >> task_run_ingestor >> task_transform
