import requests
import json
import pandas as pd
from pathlib import Path

# Load configuration file
with open("config.json", "r") as f:
    config = json.load(f)

# Extract values from config
API_KEY = config["api_key"]
LOCATIONS = config["locations"]
UNITS = config["units"]
RAW_TEMPLATE = config["raw_filename"]
PROCESSED_TEMPLATE = config["processed_filename"]

# Create directories for saving data
Path("data/raw").mkdir(parents=True, exist_ok=True)
Path("data/processed").mkdir(parents=True, exist_ok=True)

# Fetch and process weather data
for location in LOCATIONS:
    print(f"Fetching weather data for: {location}")

    # API Request
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={"q": location, "units": UNITS, "appid": API_KEY}
    )

    # Check for valid response
    if response.status_code == 200:
        data = response.json()

        # Save raw JSON
        raw_file = RAW_TEMPLATE.format(location=location)
        with open(raw_file, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Raw data saved to: {raw_file}")

        # Process and save CSV
        weather_data = {k: v for k, v in data.items() if k != "weather"}
        df = pd.json_normalize(weather_data)
        processed_file = PROCESSED_TEMPLATE.format(location=location)
        df.to_csv(processed_file, index=False)
        print(f"Processed data saved to: {processed_file}")
    else:
        print(f"Failed to fetch data for {location}. Error: {response.text}")
