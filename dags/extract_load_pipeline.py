from datetime import datetime, timedelta
from airflow import DAG

default_args = {}

with DAG(dag_id='extract_and_load', schedule_interval="0 */1 * * *", start_date=datetime(2023, 8, 4), catchup=False) as dag:
    # write you extract and load airflow dag here
    # the dag should have three bash operators
    # migration >> extract >> load
    pass
