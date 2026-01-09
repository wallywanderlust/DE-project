import requests
import csv
import os
from datetime import datetime

# API Endpoint for Open-Meteo (No API Key required!)
URL = "https://api.open-meteo.com/v1/forecast?latitude=45.7485&longitude=4.8467&current_weather=true"

def run_pipeline():
    response = requests.get(URL) #This is the API Request
    if response.status_code == 200:
        data = response.json()['current_weather'] # This is the Response
        
        # Transform: Prepare the data row
        row = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'temperature': data['temperature'],
            'windspeed': data['windspeed']
          

        }

        # Load: Save to our local "Data Lake" (CSV)
        file_path = 'data/weather_log.csv'
        file_exists = os.path.isfile(file_path)

        with open(file_path, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=row.keys())
            if not file_exists:
                writer.writeheader() # Add header only once
            writer.writerow(row)
        print(f"Data successfully logged to {file_path}")
    else:
        print("API Request Failed")

if __name__== "__main__":
    run_pipeline()