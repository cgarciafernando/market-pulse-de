# Market Pulse DE  
### Pipeline ETL de Criptomonedas

**Market Pulse DE** es un proyecto de Data Engineering orientado a la construcción de un pipeline ETL para la ingesta, transformación y visualización de datos de criptomonedas.

El objetivo es montar un flujo de datos claro y reproducible: extraer información desde la API pública de CoinGecko, almacenarla en PostgreSQL, orquestar el proceso con Airflow y exponer los resultados en Metabase para su análisis.

---

## Stack Tecnológico

- Python 3.11  
- Apache Airflow 2.7.1  
- PostgreSQL 15  
- Metabase  
- Docker Compose  

---

## Arquitectura

El flujo del sistema sigue una estructura sencilla y modular:

1. **Extracción**  
   Se consumen datos de mercado (BTC, ETH, SOL) desde la API de CoinGecko.

2. **Carga**  
   Los datos obtenidos se almacenan en una base de datos PostgreSQL.

3. **Transformación**  
   Se ejecutan scripts en Python para limpiar y estructurar la información.

4. **Orquestación**  
   Airflow gestiona la ejecución mediante el DAG `market_pulse_ingestion`.

5. **Visualización**  
   Metabase se conecta a PostgreSQL para construir dashboards y consultas analíticas.

---

## Estructura del Proyecto

    .
    ├── dags/
    │   └── market_pulse_ingestion.py
    ├── scripts/
    │   ├── ingest_data.py
    │   └── transform_data.py
    ├── docker-compose.yaml
    └── .env

---

## DAG: market_pulse_ingestion

El pipeline está compuesto por las siguientes tareas:

- `check_api_status`  
  Verifica que la API esté disponible antes de iniciar el proceso.

- `run_docker_ingestor`  
  Ejecuta el contenedor responsable de la ingesta de datos.

- `transform_data`  
  Procesa y transforma los datos almacenados en la base.

---

## Acceso a los Servicios

Una vez levantado el entorno con Docker Compose:

**Airflow**  
- URL: http://localhost:8080  
- Usuario: admin  
- Password: admin  

**Metabase**  
- URL: http://localhost:3000  
- Host de conexión a base de datos: postgres  

---

## Puesta en Marcha

1. Copiar el archivo .env.example a uno nuevo llamado .env y configurar las credenciales. 
2. Levantar los servicios:

        docker compose up -d

3. Acceder a Airflow y habilitar el DAG `market_pulse_ingestion`.  
4. Configurar Metabase conectándolo a la base de datos PostgreSQL.  

---

## Objetivo del Proyecto

Este proyecto demuestra la implementación práctica de un pipeline ETL sencillo utilizando herramientas ampliamente adoptadas en entornos de Data Engineering, con énfasis en:

- Orquestación reproducible  
- Entornos completamente containerizados  
- Separación clara entre ingesta y transformación  
- Visualización orientada a análisis de datos  

---
