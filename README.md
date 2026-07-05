# Stock Predictions

Personal stock prediction platform for practicing data engineering, analytics engineering, and machine learning workflows.

## Current foundation

This repository currently implements the first two architecture steps:

1. **Git repository organization** for source code, docs, notebooks, database initialization, dbt models, tests, and Airflow assets.
2. **Docker Compose local infrastructure** that starts PostgreSQL, Apache Airflow, and Metabase as a reproducible local mini-cloud using Python 3.12-targeted services.

## Repository layout

```text
airflow/             Airflow DAGs, plugins, config, and local logs
db/init/             PostgreSQL initialization scripts
dbt/models/          Future dbt transformation models
docs/                Project documentation
notebooks/           Jupyter exploration notebooks
python/stock_platform/ Reusable Python package code
tests/               Automated tests
```

## Runtime target

Use **Python 3.12** for local development. The Airflow services use the official `apache/airflow:3.2.2-python3.12` image, `pyproject.toml` declares `>=3.12,<3.13`, and the dependency list is selected for Python 3.12 on Ubuntu 24.04-compatible development machines.

## Quick start

1. Copy environment defaults:

   ```bash
   cp .env.example .env
   ```

2. Start the local platform:

   ```bash
   docker compose up
   ```

3. Open the Airflow API server / UI at <http://localhost:8080> and sign in with `airflow` / `airflow`.

PostgreSQL is exposed on `localhost:5432` by default. Metabase is exposed on <http://localhost:3000>. On first startup, Postgres creates the `raw`, `analytics`, and `metadata` schemas from `db/init/01_create_schemas.sql` and a separate `metabase_app` database for Metabase application metadata.

See [docs/local-development.md](docs/local-development.md) for more details.
