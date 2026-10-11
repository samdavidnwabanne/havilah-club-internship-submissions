# Day 14: Weather Forecast Checker

## API Selected
Open-Meteo (https://open-meteo.com) is a free weather API listed on PublicAPIs.io. It returns JSON from a GET request and needs no API key, so nothing secret is stored and no `.env` file is used.

## What the Program Does
The user types a city name. The program looks up that city's coordinates, requests the weather from the API, and prints the current conditions and a 7 day forecast.

Available cities: Lagos, Abuja, Kano, Port Harcourt, Enugu.

## Endpoint and Parameters
Endpoint: `https://api.open-meteo.com/v1/forecast`
Method: GET
Authentication: none

| Parameter | Value used | Purpose |
|---|---|---|
| `latitude` | city latitude | location of the city |
| `longitude` | city longitude | location of the city |
| `current_weather` | `true` | include the current conditions |
| `daily` | `temperature_2m_max,temperature_2m_min,precipitation_sum` | daily forecast values |
| `timezone` | `auto` | use the local time of the city |

Typing a different city changes the latitude and longitude, and the program processes the new response in the same way.

## JSON Structure
The response is a dictionary containing:
- `current_weather`: a dictionary with `temperature`, `windspeed`, `time`, and more
- `daily`: a dictionary of lists (`time`, `temperature_2m_max`, `temperature_2m_min`, `precipitation_sum`), where the same position in each list belongs to the same day

## Information Extracted
- Current temperature (°C)
- Current wind speed (km/h)
- Time of the reading
- Daily highest temperature
- Daily lowest temperature
- Daily rainfall total (mm)

## Error Handling
- `try` / `except requests.exceptions.RequestException` handles network failures
- `response.status_code` is checked, and anything other than 200 prints a message instead of crashing
- A city that is not in the list prints the available cities

## How to Run
```
python -m pip install requests
python week-3/day-14-python-apis/main.py
```