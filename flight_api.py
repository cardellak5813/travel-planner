import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file (to store API keys securely)
load_dotenv()

# API key and endpoint URL
FLIGHT_API_KEY = os.getenv('FLIGHT_API_KEY')
FLIGHT_API_URL = f"https://api.flightapi.io/roundtrip/{FLIGHT_API_KEY}"

def get_flight_details(departure_airport_code, arrival_airport_code, departure_date, arrival_date, adults, children, infants, cabin_class, currency):
    # Construct the full API URL with parameters
    url = f"{FLIGHT_API_URL}/{departure_airport_code}/{arrival_airport_code}/{departure_date}/{arrival_date}/{adults}/{children}/{infants}/{cabin_class}/{currency}"
    
    # Make the API request
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for any bad status codes (4xx, 5xx)
        flight_data = response.json()

        # Return the full response data for further use
        return flight_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching flight data: {e}")
        return None

# Function to extract and print unique flight prices, limiting to 5 options
def get_unique_flight_prices(data):
    """
    Extract and print unique flight prices from the flight data in a formatted way, limiting output to 5.
    """
    prices = set()  # Use a set to store unique prices

    if "itineraries" in data and data["itineraries"]:
        for itinerary in data["itineraries"]:
            if "pricing_options" in itinerary:
                for option in itinerary["pricing_options"]:
                    if "price" in option and "amount" in option["price"]:
                        price = option["price"]["amount"]
                        prices.add(price)
                    if len(prices) >= 5:  # Limit to 5 prices
                        break
            if len(prices) >= 5:
                break

    if prices:
        print("\n----- Available Flight Prices (Limited to 5 options) -----")
        for idx, price in enumerate(sorted(prices), 1):
            print(f"Option {idx}: ${price:.2f}")
        print("-----------------------------------------------------------\n")
    else:
        print("No pricing options available for this flight.")

# Example usage
if __name__ == "__main__":
    departure_airport_code = input("Enter your departure airport code (e.g., MSP): ")
    arrival_airport_code = input("Enter your arrival airport code (e.g., LAX): ")
    departure_date = input("Enter your departure date (YYYY-MM-DD): ")
    arrival_date = input("Enter your return date (YYYY-MM-DD): ")
    adults = input("Enter the number of adults: ")
    children = input("Enter the number of children: ")
    infants = input("Enter the number of infants: ")
    cabin_class = input('Enter cabin class ("Economy", "Business", "First", "Premium_Economy"): ')
    currency = input("Enter the currency (e.g., USD): ")
    
    # Fetch flight details
    flight_data = get_flight_details(departure_airport_code, arrival_airport_code, departure_date, arrival_date, adults, children, infants, cabin_class, currency)
    
    # If data is fetched successfully, extract and display the prices
    if flight_data:
        get_unique_flight_prices(flight_data)
    else:
        print("No flight data available.")
