# Day 14 — Python and APIs
# Task: Build a Python program that retrieves information from an API
# and processes the JSON response to produce a useful output.
# Submit this script + a screenshot of the printed output.

import requests
import os

# Load your API key from the environment (never hardcode it here).
# Copy .env.example to .env and fill in your key before running.
# Open-Meteo is free and needs no key, so API_KEY is not used in this program.
API_KEY = os.getenv("API_KEY", "")
BASE_URL = "https://api.open-meteo.com/v1/forecast"

# Open-Meteo works with coordinates, so each city is stored with its
# latitude and longitude
CITIES = {
    "lagos": {"name": "Lagos", "latitude": 6.5244, "longitude": 3.3792},
    "abuja": {"name": "Abuja", "latitude": 9.0765, "longitude": 7.3986},
    "kano": {"name": "Kano", "latitude": 12.0022, "longitude": 8.5920},
    "port harcourt": {"name": "Port Harcourt", "latitude": 4.8156, "longitude": 7.0498},
    "enugu": {"name": "Enugu", "latitude": 6.4584, "longitude": 7.5464},
}


# Step 1: Fetch Data
# Make a GET request to the API and return the parsed JSON response.
# Handle network errors and non-200 status codes gracefully.

def fetch_data(query):
    city = query.strip().lower()

    # Edge case: the city is not in our list
    if city not in CITIES:
        print("City not found. Available cities:")
        for key in CITIES:
            print(CITIES[key]["name"])
        return None

    # Build the params dictionary for the request
    params = {
        "latitude": CITIES[city]["latitude"],
        "longitude": CITIES[city]["longitude"],
        "current_weather": "true",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto",
    }

    # timeout=10 stops the program waiting forever if the network is slow
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
    except requests.exceptions.RequestException:
        print("Network error: could not connect to the weather service.")
        return None

    # Check the request that was sent and the status code that came back
    print("Request URL:", response.url)
    print("Status code:", response.status_code)

    # Only call .json() when the request succeeded
    if response.status_code != 200:
        print("The API did not return a successful response.")
        return None

    data = response.json()
    # print(data)    # uncomment this to inspect the structure of the JSON

    # Add the city name so display_results() can show it
    data["city"] = CITIES[city]["name"]
    return data


# Step 2: Parse and Display
# Extract at least 3 useful pieces of information from the response.
# Print them in a clear, labelled format — not raw JSON.

def display_results(data):
    current = data["current_weather"]    # a dictionary
    daily = data["daily"]                # a dictionary of lists

    print("\nWeather Report:", data["city"])

    print("\nCurrent Conditions")
    print("Temperature:", current["temperature"], "°C")
    print("Wind speed:", current["windspeed"], "km/h")
    print("Time:", current["time"])

    # The same position in each list belongs to the same day
    print("\n7 Day Forecast")
    for index in range(len(daily["time"])):
        date = daily["time"][index]
        highest = daily["temperature_2m_max"][index]
        lowest = daily["temperature_2m_min"][index]
        rain = daily["precipitation_sum"][index]
        print(f"{date}: High {highest} °C, Low {lowest} °C, Rain {rain} mm")


# Main
def main():
    query = input("Enter your search query: ")
    data = fetch_data(query)
    if data:
        display_results(data)


if __name__ == "__main__":
    main() 