from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime 

dag = DAG('dag_pool', description = "Pools", schedule_interval=None, start_date = datetime(2023,3,4), catchup=False)

task1 = BashOperator(task_id = "tsk1", bash_command="sleep 5", pool="my_pool", priority_weight = 5, dag=dag)
task2 = BashOperator(task_id = "tsk2", bash_command="sleep 5", pool="my_pool", dag=dag)
task3 = BashOperator(task_id = "tsk3", bash_command="sleep 5", pool="my_pool", priority_weight = 10, dag=dag)
task4 = BashOperator(task_id = "tsk4", bash_command="sleep 5", pool="my_pool", dag=dag)

