# 🌦️ Weather Data ETL Pipeline

## Overview
This project is a functional **ETL (Extract, Transform, Load)** pipeline. It automates the collection of weather data, processes it for consistency, and stores it in a local **Data Lake** for future analysis.

## 🛠️ The Data Stack
* **Extract**: Python `requests` library pulling from the Open-Meteo REST API.
* **Transform**: Data cleaning and timestamping to ensure **Data Lineage**.
* **Load**: Persistent storage in a CSV-based **Data Lake**.
* **Modeling**: SQL Star Schema design for **Data Warehousing**.

## 🚀 How to Run
1. **Clone the repo**: `git clone https://github.com/wallywanderlust/DE-project.git`
2. **Install dependencies**: `pip install requests`
3. **Execute the pipeline**: `python scripts/fetch_weather.py`
4. **View results**: Check `data/weather_log.csv`

## 🧠 Key Learnings
- Managing **API Responses** and handling HTTP status codes.
- Resolving complex **Git merge conflicts** and branch rebasing.
- Designing a **Star Schema** with Fact and Dimension tables to optimize query performance.

Setup Environment: Create a virtual environment and install dependencies.


Database Setup: Ensure Postgres is running and the schema is created.


Execute: Run the main Python script or trigger the Airflow DAG.
