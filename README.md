# E-Commerce Data Platform — ShopFlow

An end-to-end data engineering project that ingests e-commerce data, stores raw data in a data lake, transforms it, and prepares analytical datasets for reporting and business intelligence.

## Architecture

FastAPI → Python Ingestion → MinIO → PySpark → PostgreSQL → dbt → Metabase

**Orchestration:** Apache Airflow
**Infrastructure:** Docker Compose

## Tech Stack

- **Python & FastAPI** — API and data ingestion
- **MinIO** — S3-compatible raw data lake
- **PySpark** — Data transformation
- **PostgreSQL** — Relational database and analytical storage
- **dbt** — SQL transformations, analytical marts and data quality tests
- **Apache Airflow** — Workflow orchestration
- **Metabase** — Data exploration and BI dashboards
- **Docker Compose** — Local infrastructure
- **PowerShell** — Local development and database administration
- **Git & GitHub** — Version control

## Project Structure

```text
e-commerce_data_platform/
├── api/                  # API application
├── src/                  # Ingestion and supporting Python modules
├── sql/                  # Database schema and SQL scripts
├── spark/                # Spark transformation jobs
├── dbt/
│   └── shopflow/         # dbt models, marts and tests
├── airflow/              # Workflow orchestration
├── tests/                # Automated tests
├── docker-compose.yml
├── .env.example
└── README.md
```

## Data Pipeline

1. **Ingestion:** Python and FastAPI handle data ingestion.
2. **Raw storage:** Raw data is stored in MinIO.
3. **Transformation:** PySpark processes data for downstream use.
4. **Database loading:** PostgreSQL stores relational and analytical data.
5. **Data modelling:** dbt creates staging models, intermediate models and analytical marts, supported by data quality tests.
6. **Orchestration:** Airflow coordinates pipeline tasks and integrates with the Windows environment via SSH.
7. **Analytics:** Metabase provides dashboards and business insights based on the analytical datasets.

## Getting Started

### Requirements

- Docker Desktop
- Python
- Java and Spark dependencies for local Spark jobs
- dbt with the PostgreSQL adapter
- Git

### Start the infrastructure

From the project root:

```powershell
docker compose up -d
```

Check running containers:

```powershell
docker ps
```

### Initialise the PostgreSQL schema

From the project root, execute the SQL schema through PowerShell:

```powershell
Get-Content .\sql\schema.sql | docker exec -i shopflow-postgres psql -U shopflow -d shopflow
```

The `-i` option keeps standard input open so the SQL file can be piped into the container. The `-t` option allocates a pseudo-terminal and is unnecessary for this non-interactive operation.

For an interactive PostgreSQL session:

```powershell
docker exec -it shopflow-postgres psql -U shopflow -d shopflow
```

These commands assume the container is named `shopflow-postgres`, the database is `shopflow`, and the database user is `shopflow`.

## dbt

The dbt project is located in `dbt/shopflow/`.

It includes staging models, intermediate transformations, analytical marts and data quality tests.

Typical commands, executed from the directory containing `dbt_project.yml`:

```powershell
dbt debug
dbt run
dbt test
dbt build
```

## Current Progress

- [x] API and data ingestion
- [x] Raw data storage in MinIO
- [x] PostgreSQL schema and data loading
- [x] dbt staging models
- [x] Intermediate dbt models
- [x] Analytical marts
- [x] Initial dbt data quality tests
- [x] Airflow workflow orchestration
- [x] Airflow integration with the Windows environment via SSH
- [x] Metabase analytics and BI dashboards
- [ ] Continuous integration

## Security

- Store credentials and environment variables locally.
- Never commit real secrets or `.env` files to version control.
- Use `.env.example` as a template without real credentials.
- Grant only the permissions required by each service.

## Project Goals

This project demonstrates practical data engineering skills across data ingestion, data lake storage, distributed processing, relational databases, analytics engineering, workflow orchestration, business intelligence, containerisation and data quality testing.
