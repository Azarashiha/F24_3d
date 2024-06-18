import json
import time
from FlightRadar24.api import FlightRadar24API

def get_flight_data():
    fr_api = FlightRadar24API()
    # 特定のポイント周辺のフライトを取得（例：東京周辺）
    bounds = fr_api.get_bounds_by_point(35.5494, 139.7817, 200000)  # 半径20km
    flights = fr_api.get_flights(bounds=bounds)
    
    flight_data = []
    
    for flight in flights:
        flight_info = {
            "id": flight.id,
            "lat": flight.latitude,
            "lng": flight.longitude,
            "altitude": flight.altitude,
            "direction": flight.heading,
            "callsign": flight.callsign,
            "origin_name": flight.origin_airport_iata,
            "destination_name": flight.destination_airport_iata
        }
        flight_data.append(flight_info)
    
    return flight_data

def save_flight_data():
    flight_data = get_flight_data()
    if not flight_data:
        print("No flight data retrieved")
    else:
        with open('flight_data.json', 'w') as f:
            json.dump(flight_data, f)

if __name__ == "__main__":
    while True:
        save_flight_data()
        time.sleep(1)
