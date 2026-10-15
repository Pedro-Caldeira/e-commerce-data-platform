# E-Commerce Data Platform

An end-to-end data engineering project that ingests e-commerce data, stores raw data in a data lake, transforms it, and prepares analytical datasets for reporting.

## Architecture

FastAPI → Python Ingestion → MinIO (Raw Data Lake) → PySpark → PostgreSQL → dbt → Analytics

## Tech Stack

- **Python & FastAPI** — API and data ingestion
- **MinIO** — S3-compatible raw data lake
- **PySpark** — Data transformation
- **PostgreSQL** — Relational database and analytical storage
- **dbt** — SQL transformations and data quality tests
- **Docker Compose** — Local infrastructure
- **Git & GitHub** — Version control

## Project Structure

- `api/` — API application
- `src/` — Ingestion and supporting Python modules
- `sql/` — Database schema and SQL scripts
- `spark/` — Spark transformation jobs
- `dbt/shopflow/` — dbt project, staging and intermediate models
- `airflow/` — Workflow orchestration
- `tests/` — Automated tests

## Current Progress

- [x] API and data ingestion
- [x] Raw data storage in MinIO
- [x] PostgreSQL schema and data loading
- [x] dbt staging models
- [x] First intermediate dbt model
- [x] Initial dbt data quality tests
- [ ] Analytical marts
- [ ] Workflow orchestration
- [ ] BI dashboards
- [ ] Continuous integration

## Getting Started

Requirements:
- Docker Desktop
- Python
- Java and Spark dependencies for local Spark jobs
- dbt with the PostgreSQL adapter

Configuration and execution instructions will be documented as the project evolves.

## Security

Credentials and environment variables are stored locally and must never be committed to version control. Use `.env.example` as a template without real secrets.