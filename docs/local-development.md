# Local Development

## First-time setup

1. Copy the example environment file:

   ```bash
   cp .env.example .env
   ```

2. Start the local infrastructure:

   ```bash
   docker compose up
   ```

3. Open Airflow at <http://localhost:8080> and sign in with `airflow` / `airflow`.

## Optional tools

Start pgAdmin with the `tools` profile:

```bash
docker compose --profile tools up pgadmin
```

pgAdmin is available at <http://localhost:5050> using the credentials from `.env`.

## Services

- `postgres`: local operational database / warehouse.
- `airflow-init`: runs Airflow database migrations and creates the local admin user.
- `airflow-webserver`: Airflow UI.
- `airflow-scheduler`: Airflow scheduler.
- `pgadmin`: optional Postgres UI.
