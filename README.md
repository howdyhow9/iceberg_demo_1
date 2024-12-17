# Modern Data Lake with Trino, Spark, and Iceberg

This project sets up a modern data lake environment using Trino, Spark, and Apache Iceberg for data warehousing, with MinIO as the object storage backend.

## Architecture Overview

The system consists of the following components:

- **Trino (v457)**: SQL query engine for data analysis
- **Apache Spark**: Distributed processing engine
- **Apache Iceberg**: Table format for large analytic datasets
- **MinIO**: S3-compatible object storage
- **Apache Hive Metastore**: Metadata management service
- **PostgreSQL**: Backend database for Hive Metastore

## Prerequisites

- Docker and Docker Compose v3.8+
- At least 8GB of RAM available for the containers
- Port availability: 8080, 8081, 9000, 9001, 9083, 5432, 7077, 4040

## Quick Start

1. Clone this repository
2. Create the required directories:
   ```bash
   mkdir -p data/iceberg/osdp/spark-warehouse postgres-data
   ```
3. Start the services:
   ```bash
   docker-compose up -d
   ```

## Service Details

### Trino
- Query interface available at `http://localhost:8081`
- Configured for Iceberg catalog via Hive Metastore
- S3 connection configured for MinIO backend

### Spark
- Master UI available at `http://localhost:8080`
- Job tracking UI at `http://localhost:4040`
- Configuration:
    - Master: spark://spark:7077
    - Driver Memory: 2GB
    - Executor Memory: 2GB
    - Max Cores: 2
    - Worker Memory: 2GB

### MinIO
- S3-compatible storage
- API endpoint: `http://localhost:9000`
- Console UI: `http://localhost:9001`
- Default credentials:
    - Username: minioadmin
    - Password: minioadmin
- Preconfigured bucket: `iceberg-lake`

### Hive Metastore
- Running on port 9083
- PostgreSQL backend on port 5432
- Credentials:
    - Database: hive_metastore
    - Username: hive
    - Password: hivepass123

## Usage

Run Spark Scripts:
### Run the Spark SQL session script
```bash
docker-compose exec spark python3 /opt/spark/work-dir/scripts/spark_sql_session_iceberg.py
```
### Submit a basic Spark job
```bash
docker-compose exec spark spark-submit /opt/spark/work-dir/scripts/basic_spark_iceberg.py
```
### Access Trino:
sqlCopy-- Connect to Trino on port 8081
-- Use the iceberg catalog
USE iceberg.default;

### Access Spark:

Place your Spark scripts in the ./scripts directory
They will be available in the container at /opt/spark/work-dir/scripts


### Access MinIO:

Use the web console at http://localhost:9001
Use S3-compatible tools with endpoint http://localhost:9000

## Maintenance

- Monitor the logs:
  ```bash
  docker-compose logs -f [service_name]
  ```
- Restart services:
  ```bash
  docker-compose restart [service_name]
  ```
- Reset everything:
  ```bash
  docker-compose down -v
  rm -rf postgres-data data
  ```
