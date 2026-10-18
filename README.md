# E-Commerce Data Platform — ShopFlow

An end-to-end data engineering project that ingests e-commerce data, stores raw data in a data lake, transforms it with PySpark, loads it into PostgreSQL, and builds analytical models with dbt. Apache Airflow orchestrates the pipeline from ingestion to analytics.

## Architecture

```text
FastAPI
   ↓
Python Ingestion
   ↓
MinIO (Raw Data Lake)
   ↓
PySpark Transformations
   ↓
PostgreSQL
   ↓
dbt (Data Modeling & Testing)
   ↓
Analytics with Metabase
```

**Orchestration:** Apache Airflow coordinates ingestion, Spark jobs, and dbt execution through a scheduled DAG. Airflow runs in Docker and connects to the Windows host through SSH to execute the Python and Spark jobs.

## Tech Stack

- **Python** — Ingestion, data processing, and supporting modules
- **FastAPI** — E-commerce API
- **MinIO** — S3-compatible object storage for raw data
- **PySpark** — Data transformation jobs
- **PostgreSQL** — Relational database and analytical storage
- **dbt** — SQL transformations, data modeling, and data quality tests
- **Apache Airflow** — Workflow orchestration and scheduling
- **Metabase** — Business intelligence and data visualization
- **Docker Compose** — Local infrastructure and services
- **Git & GitHub** — Version control and project collaboration

## Project Structure

```text
e-commerce_data_platform/
├── api/                  # FastAPI application
├── src/                  # Ingestion and supporting Python modules
├── sql/                  # SQL schemas and scripts
├── spark/                # PySpark transformation jobs
├── dbt/
│   └── shopflow/         # dbt project and data models
├── airflow/
│   ├── dags/             # Airflow DAG definitions
│   ├── logs/             # Airflow logs
│   ├── plugins/          # Airflow plugins
│   └── docker-compose.yml
├── tests/                # Automated tests
├── docker-compose.yml    # Main infrastructure
├── .env.example          # Environment variable template
└── README.md
```

## Pipeline Workflow

The `shopflow_pipeline` DAG orchestrates the following tasks in sequence:

1. **Data ingestion** — Extracts customers, products, orders, and payments from the API.
2. **Raw data storage** — Stores ingested JSON data in MinIO.
3. **Customers transformation** — Runs the customers PySpark job.
4. **Products transformation** — Runs the products PySpark job.
5. **Orders transformation** — Runs the orders PySpark job.
6. **Payments transformation** — Runs the payments PySpark job.
7. **dbt build** — Builds the configured dbt models and runs their associated tests.

The DAG is configured for scheduled execution. Its schedule and timezone are defined in the DAG configuration.

## Current Progress

- [x] FastAPI application and data ingestion
- [x] Retry and pagination logic for API extraction
- [x] Raw data storage in MinIO
- [x] PostgreSQL schema and data loading
- [x] PySpark transformation jobs for customers, products, orders, and payments
- [x] dbt staging models
- [x] Initial intermediate dbt model
- [x] Initial dbt data quality tests
- [x] Apache Airflow deployed with Docker Compose
- [x] SSH connection from Airflow to the Windows host
- [x] Integrated ingestion, Spark, and dbt pipeline
- [x] Successful manual pipeline execution in Airflow
- [x] Automatic DAG scheduling configured
- [x] Initial Metabase dashboard
- [ ] Analytical marts and additional business metrics
- [ ] Expanded data quality and integration tests
- [ ] GitHub Actions CI/CD
- [ ] Production-oriented deployment and secrets management

## Getting Started

### Requirements

- Docker Desktop
- Python and a project virtual environment
- Java and the dependencies required for local PySpark execution
- PySpark and its required Hadoop utilities for the Windows environment
- dbt with the PostgreSQL adapter
- Git

### Configuration

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the project dependencies.
4. Create a local `.env` file using `.env.example` as a template.
5. Configure MinIO and PostgreSQL connection settings.
6. Configure the dbt profile in `~/.dbt/profiles.yml`.
7. Configure the Airflow SSH connection to the Windows host.
8. Start the main services using Docker Compose.
9. Start Airflow using `airflow/docker-compose.yml`.

**Important:** The project currently uses a local development setup. Paths, credentials, ports, and SSH settings may need to be adapted to your machine. Do not commit `.env`, private SSH keys, or files containing real credentials.

### Running the Pipeline

The pipeline is managed through the Airflow web interface:

- Airflow: `http://localhost:8080`
- Metabase: `http://localhost:3000`
- MinIO Console: `http://localhost:9001`

Run the `shopflow_pipeline` DAG manually for testing or let its configured schedule trigger executions automatically. Ensure Docker, Airflow, PostgreSQL, MinIO, and the Windows SSH service are available when the DAG runs.

### Running dbt Separately

From the repository root, with the project virtual environment configured:

```powershell
.\.venv\Scripts\dbt.exe debug --project-dir ".\dbt\shopflow"
.\.venv\Scripts\dbt.exe build --project-dir ".\dbt\shopflow"
```

The `debug` command checks the dbt project and connection configuration. The `build` command runs the selected models and their configured tests.

## Security

- Keep credentials and environment variables in local configuration files.
- Never commit `.env`, private SSH keys, passwords, or production secrets.
- Use `.env.example` as a template with placeholder values only.
- Keep `profiles.yml` outside the repository when it contains credentials.
- Use proper SSH host-key verification and managed secrets in production.
- Replace development credentials before exposing services outside your local environment.

## Future Improvements

- Build analytical marts for sales, products, customers, and order performance.
- Expand dbt tests, documentation, and model lineage.
- Improve Airflow failure handling, retries, alerts, and monitoring.
- Add automated CI checks with GitHub Actions.
- Containerize and standardize execution environments.
- Prepare deployment configuration for a production environment.
