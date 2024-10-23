import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file (to store API keys securely)
load_dotenv()

# Replace with your actual FlightAPI endpoint and API key
FLIGHT_API_KEY = os.getenv('FLIGHT_API_KEY')
FLIGHT_API_URL = "https://api.flightapi.io/"

def get_flight_details(origin, destination, departure_date, return_date):
    # Set up the API query parameters
    params = {
        'origin': origin,
        'destination': destination,
        'departure_date': departure_date,
        'return_date': return_date,
        'api_key': FLIGHT_API_KEY,
    }
    
    # Make the API request
    try:
        response = requests.get(FLIGHT_API_URL, params=params)
        response.raise_for_status()
        flight_data = response.json()

        # Handle the flight data (parse and return details)
        flights = []
        for flight in flight_data['flights']:
            flight_info = {
                'airline': flight['airline'],
                'flight_number': flight['flight_number'],
                'departure_time': flight['departure_time'],
                'arrival_time': flight['arrival_time'],
                'price': flight['price'],
            }
            flights.append(flight_info)
        
        return flights
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching flight data: {e}")
        return None

# Example usage
if __name__ == "__main__":
    origin = input("Enter your origin city code (e.g., JFK for New York): ")
    destination = input("Enter your destination city code (e.g., LAX for Los Angeles): ")
    departure_date = input("Enter your departure date (YYYY-MM-DD): ")
    return_date = input("Enter your return date (YYYY-MM-DD): ")
    
    flights = get_flight_details(origin, destination, departure_date, return_date)
    
    if flights:
        print("Available Flights:")
        for flight in flights:
            print(f"Airline: {flight['airline']}, Flight: {flight['flight_number']}, "
                  f"Departure: {flight['departure_time']}, Arrival: {flight['arrival_time']}, "
                  f"Price: {flight['price']}")
    else:
        print("No flight data available.")
