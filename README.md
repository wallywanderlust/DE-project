Weather Data Pipeline (ETL)

📌 Project Overview
This project is a functional Data Pipeline designed to automate the collection, transformation, and storage of weather data. It demonstrates the transition from Ad Hoc scripts to a Scheduled workflow using industry-standard tools.




🏗️ Architecture
The pipeline follows a standard ETL (Extract, Transform, Load) pattern:


Extract: Fetches raw JSON data from an external API (Open-Meteo).



Transform: Cleans the data, handles missing values (Data Enrichment), and converts units.



Load: Stores the structured data into a Postgres database using ACID compliant transactions.



🛠️ Tech Stack

Language: Python (Bash for environment setup).


Database: Postgres (Relational storage).



Orchestration: Apache Airflow (Workflow management).



Version Control: Git.


📊 Data Model
The project uses a Star Schema to optimize for analytical queries:



Fact Table: weather_readings (stores hourly temperature, wind speed, etc.).


Dimension Table: locations (stores city name, latitude, and longitude).


🚀 Key Engineering Concepts Applied

Idempotency: The pipeline is designed so that running the same task multiple times produces the same result, preventing duplicate data.


Atomicity: Using ACID principles to ensure that if a data load fails, the database rolls back to its previous state.


Data Lineage: Tracking the origin and movement of data from the API to the final Database.


DRY Principle: Code is written following the Don't Repeat Yourself standard for better maintainability.

🚦 How to Run

Clone the Repo: git clone [your-repo-link].

Setup Environment: Create a virtual environment and install dependencies.


Database Setup: Ensure Postgres is running and the schema is created.


Execute: Run the main Python script or trigger the Airflow DAG.
