import os
from datetime import datetime
from pathlib import Path

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping


here = Path(__file__).resolve().parent
project_dir = here / "dbt" / "snowflake_dbt_airflow"   # <-- contains dbt_project.yml

profile_config = ProfileConfig(
    profile_name = 'default',
    target_name = 'dev',
    profile_mapping = SnowflakeUserPasswordProfileMapping(
        conn_id = "snowflake_conn",
        profile_args = {"database":"dbt_db", "schema":"dbt_schema"},
    )
)

dbt_snowflake_dag = DbtDag(
    project_config = ProjectConfig(str(project_dir)),
    operator_args = {"install_deps":True},
    profile_config = profile_config,
    execution_config=ExecutionConfig(dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",),
    schedule_interval="@daily",
    start_date=datetime(2025, 8, 16),
    catchup=False,
    dag_id="snowflake_dbt_airflow"
)