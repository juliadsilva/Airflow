from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime 

dag = DAG('dag_02', description = 'Segunda dag - Paralelismo', schedule_interval=None, start_date = datetime(2023,3,4), catchup=False)

task1 = BashOperator(task_id = "tsk1", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id = "tsk2", bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id = "tsk3", bash_command="sleep 5", dag=dag)

task1 >> [task2,task3]

