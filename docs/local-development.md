# Local Development

## Runtime target

Use Python 3.12 for local virtual environments and notebooks. The Docker Compose stack uses the official `apache/airflow:3.2.2-python3.12` image, the official `metabase/metabase` Docker image, plus Debian/Ubuntu-friendly container variants such as `postgres:17-bookworm`, so the setup is well aligned with Ubuntu 24.04 development machines without requiring a custom Airflow image.

## First-time setup

1. Copy the example environment file:

   ```bash
   cp .env.example .env
   ```

2. Start the local infrastructure:

   ```bash
   docker compose up
   ```

3. Open the Airflow API server / UI at <http://localhost:8080> and sign in with `airflow` / `airflow`.

4. Open Metabase at <http://localhost:3000> and complete the first-run setup wizard. When adding the stock project database as a data source, use these values:

   - **Host**: `postgres`
   - **Port**: `5432`
   - **Database name**: `stock_predictions`
   - **Username/password**: the stock Postgres credentials from `.env`
   - **Schemas**: select only `raw`, `analytics`, and `metadata`

## Local PostgreSQL containers

The Compose stack intentionally keeps application metadata out of the stock project database:

- `postgres` (`stock-postgres`) owns the stock project database `stock_predictions`, mounts only `db/init`, and is the only Postgres service exposed on `localhost:5432`.
- `airflow-postgres` (`stock-airflow-postgres`) owns Airflow metadata in `airflow_metadata` and stores it in the `airflow-postgres-data` Docker volume. Airflow services connect to this service, not to the stock database.
- `metabase-postgres` (`stock-metabase-postgres`) owns Metabase application metadata in `metabase_application_metadata` and stores it in the `metabase-postgres-data` Docker volume. Metabase uses this for its internal app state; add `postgres` separately as the stock data source in the Metabase UI.

## Airflow DAG discovery

Airflow mounts local DAG files from `./airflow/dags` into `/opt/airflow/dags`. The stack also runs a dedicated `airflow-dag-processor` service for Airflow 3, so new DAG files created under `airflow/dags` are parsed without rebuilding containers.

During `airflow-init`, the container starts as root long enough to create `/opt/airflow/logs/dag_processor_manager` and fix ownership/permissions on the mounted Airflow directories. This prevents DAG processor log write failures that can stop DAG parsing, including the `platform_smoke_test` DAG.

## Resetting existing local volumes

If you previously ran the older stack, your local `postgres-data` volume may already contain Airflow metadata tables and a Metabase application database inside `stock_predictions` or the stock Postgres instance. To reset the local development state and recreate the three separated databases, stop the stack and remove the project volumes:

```bash
docker compose down --volumes
```

Then start fresh:

```bash
docker compose up
```

This deletes local container databases, so export anything you want to keep first.

## Optional tools

Start pgAdmin with the `tools` profile:

```bash
docker compose --profile tools up pgadmin
```

pgAdmin is available at <http://localhost:5050> using the credentials from `.env`.

## Services

- `postgres`: stock operational database / warehouse only.
- `airflow-postgres`: Airflow metadata database.
- `metabase-postgres`: Metabase application metadata database.
- `airflow-init`: fixes Airflow mount permissions, runs Airflow database migrations, and creates the local admin user.
- `airflow-api-server`: Airflow 3 API server and UI.
- `airflow-scheduler`: Airflow scheduler.
- `airflow-dag-processor`: parses DAG files for Airflow 3.
- `airflow-triggerer`: supports deferrable Airflow tasks.
- `metabase`: local BI/dashboarding UI backed by `metabase-postgres` for application metadata.
- `pgadmin`: optional Postgres UI.
