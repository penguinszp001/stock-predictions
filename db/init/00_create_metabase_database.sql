-- Separate Metabase application metadata from the stock prediction database.
-- This script runs only when the Postgres Docker volume is first initialized.
SELECT 'CREATE DATABASE metabase_app'
WHERE NOT EXISTS (
    SELECT FROM pg_database WHERE datname = 'metabase_app'
)\gexec
