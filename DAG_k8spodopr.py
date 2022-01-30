import datetime
from airflow import models
from airflow.kubernetes.secret import Secret
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator

YESTERDAY = datetime.datetime.now() - datetime.timedelta(days=1)

with models.DAG(
        dag_id='ssp-2.3',
        schedule_interval=datetime.timedelta(days=1),
        start_date=YESTERDAY) as dag:

    kubernetes_min_pod = KubernetesPodOperator(
        task_id='pod-ex-minimum',
        name='pod-ex-minimum',
        cmds=['echo'],
        namespace='default',
        image='gcr.io/vital-folder-331713/ssp-2.3',
        env_vars={'ts': '{{ ts }}'})