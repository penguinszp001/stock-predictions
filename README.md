# Stock Predictions

Personal stock prediction platform for practicing data engineering, analytics engineering, and machine learning workflows.

## Current foundation

This repository currently implements the first two architecture steps:

1. **Git repository organization** for source code, docs, notebooks, database initialization, dbt models, tests, and Airflow assets.
2. **Docker Compose local infrastructure** that starts PostgreSQL and Apache Airflow as a reproducible local mini-cloud.

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

## Quick start

1. Copy environment defaults:

   ```bash
   cp .env.example .env
   ```

2. Start the local platform:

   ```bash
   docker compose up
   ```

3. Open Airflow at <http://localhost:8080> and sign in with `airflow` / `airflow`.

PostgreSQL is exposed on `localhost:5432` by default. On first startup it creates the `raw`, `analytics`, and `metadata` schemas from `db/init/01_create_schemas.sql`.

See [docs/local-development.md](docs/local-development.md) for more details.
