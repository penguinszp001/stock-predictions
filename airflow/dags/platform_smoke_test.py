"""Minimal DAG used to verify that the local Airflow scheduler can run tasks."""

from __future__ import annotations

from datetime import datetime

from airflow.decorators import dag, task


@dag(
    dag_id="platform_smoke_test",
    description="Confirms the local Airflow infrastructure is running.",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["smoke-test", "local"],
)
def platform_smoke_test() -> None:
    """Create a small no-op workflow for local infrastructure testing."""

    @task
    def confirm_platform_ready() -> str:
        return "Stock prediction platform Airflow smoke test completed."

    confirm_platform_ready()


platform_smoke_test()
