import requests
import json
import yaml
from app.logger import setup_logger

logger = setup_logger()

def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)

def fetch_data(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

def save_data(data, output_file):
    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

def main():
    logger.info("Application started")

    try:
        config = load_config()
        api_url = config["api"]["url"]
        output_file = config["output"].get("filename", "data.json")

        logger.info("Calling API")
        data = fetch_data(api_url)

        logger.info("Saving data to JSON file")
        save_data(data, output_file)

        print("Data fetched and saved successfully!")
        logger.info("Application finished successfully")

    except Exception as e:
        logger.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
