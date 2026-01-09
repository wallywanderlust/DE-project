CREATE TABLE dim_locations (
    city_id SERIAL PRIMARY KEY,
    city_name VARCHAR(100),
    latitude FLOAT,
    longitude FLOAT
);

CREATE TABLE fact_weather (
    reading_id SERIAL PRIMARY KEY,
    city_id INT REFERENCES dim_locations(city_id),
    temperature FLOAT,
    windspeed FLOAT,
    recorded_at TIMESTAMP
);