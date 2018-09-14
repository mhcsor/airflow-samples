from datetime import datetime
from airflow import DAG
from airflow.operators.sample_plugin import SampleOperator
from airflow.operators.sample_plugin import SampleSensor


args = {
    'owner': 'airflow',
    'start_date': datetime(2017, 9, 10, 0, 0),
    'random_logic': False
}

dag = DAG(
    'sample_dag',
    schedule_interval="@once",
    default_args=args
)

with dag:
    t1 = SampleOperator(
        task_id='sample_operator'
    )

    t2 = SampleSensor(
        task_id='sample_sensor',
        run_id="{{ task_instance.xcom_pull('sample_operator', key='return_value') }}"
    )

    t1 >> t2