from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from datetime import datetime 

dag = DAG('dag_variavel', description = "Variavies", schedule_interval=None, start_date = datetime(2023,3,4), catchup=False)

def print_variable():
    minha_var = Variable.get("var_dags")
    print("O valor da variavel é ", minha_var)
    
task1 = PythonOperator(task_id = "tsk1",  python_callable = print_variable, dag=dag)

task1 




