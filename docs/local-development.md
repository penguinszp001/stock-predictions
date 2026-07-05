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

4. Open Metabase at <http://localhost:3000> and complete the first-run setup wizard. When adding the project database as a data source, use `postgres` as the host, `5432` as the port, and the Postgres credentials from `.env`.

## Optional tools

Start pgAdmin with the `tools` profile:

```bash
docker compose --profile tools up pgadmin
```

pgAdmin is available at <http://localhost:5050> using the credentials from `.env`.

## Services

- `postgres`: local operational database / warehouse.
- `airflow-init`: runs Airflow database migrations and creates the local admin user.
- `airflow-api-server`: Airflow 3 API server and UI.
- `airflow-scheduler`: Airflow scheduler.
- `airflow-dag-processor`: parses DAG files for Airflow 3.
- `airflow-triggerer`: supports deferrable Airflow tasks.
- `metabase`: local BI/dashboarding UI backed by the `metabase_app` Postgres application database.
- `pgadmin`: optional Postgres UI.
