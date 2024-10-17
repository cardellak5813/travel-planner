import requests

API_KEY = 'AIzaSyBxxVlzimuQswhNmahpMLq676sVjt8luIc'
BASE_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

def get_local_attractions(location, radius=1000, type='tourist_attraction'):
    params = {
        'location': location,
        'radius': radius,
        'type': type,
        'key': API_KEY
    }
    
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        results = response.json().get('results', [])
        attractions = [place['name'] for place in results]
        return attractions, results
    else:
        return [], []

if __name__ == "__main__":
    user_location_name = input("Enter your location: ")
    # params dictionary is not used in geocoding request, removing it
    # Geocoding the location name to get latitude and longitude
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={user_location_name}&key={API_KEY}"
    geocode_response = requests.get(geocode_url)
    
    if geocode_response.status_code == 200:
        geocode_results = geocode_response.json().get('results', [])
        if geocode_results:
            location = geocode_results[0]['geometry']['location']
            user_location = f"{location['lat']},{location['lng']}"
        else:
            print("Location not found.")
            exit(1)
    else:
        print("Error in geocoding the location.")
        exit(1)
    attractions, results = get_local_attractions(user_location)
    print("Local Attractions:")
    API_KEY = 'AIzaSyBxxVlzimuQswhNmahpMLq676sVjt8luIc'
    BASE_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

    def get_local_attractions(location, radius=1000, type='tourist_attraction'):
        params = {
            'location': location,
            'radius': radius,
            'type': type,
            'key': API_KEY
        }
        
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            results = response.json().get('results', [])
            attractions = [place['name'] for place in results]
            return attractions, results
        else:
            return [], []

    if __name__ == "__main__":
        user_location_name = input("Enter your location: ")
        # Geocoding the location name to get latitude and longitude
        geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={user_location_name}&key={API_KEY}"
        geocode_response = requests.get(geocode_url)
        
        if geocode_response.status_code == 200:
            geocode_results = geocode_response.json().get('results', [])
            if geocode_results:
                location = geocode_results[0]['geometry']['location']
                user_location = f"{location['lat']},{location['lng']}"
            else:
                print("Location not found.")
                exit(1)
        else:
            print("Error in geocoding the location.")
            exit(1)
        
        attractions, results = get_local_attractions(user_location)
        print("Local Attractions:")
        printed_attractions = set()
        for attraction in attractions:
            if attraction not in printed_attractions:
                printed_attractions.add(attraction)
                place_id = next((place['place_id'] for place in results if place['name'] == attraction), None)
                if place_id:
                    details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={API_KEY}"
                    details_response = requests.get(details_url)
                    if details_response.status_code == 200:
                        details_result = details_response.json().get('result', {})
                        reviews = details_result.get('reviews', [])
                        rating = details_result.get('rating', 'No rating')
                        print(f"{attraction}: Rating {rating}/5")
                        if not reviews:
                            print(f"{attraction}: No reviews found.")
    for attraction in attractions:
        if attraction not in printed_attractions:
            printed_attractions.add(attraction)
            place_id = next((place['place_id'] for place in results if place['name'] == attraction), None)
            if place_id:
                details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={API_KEY}"
                details_response = requests.get(details_url)
                if details_response.status_code == 200:
                    details_result = details_response.json().get('result', {})
                    reviews = details_result.get('reviews', [])
                    print(f"{attraction}:")
                    rating = details_result.get('rating', 'No rating')
                    print(f"{attraction}: Rating {rating}/5")
                    if not reviews:
                        print(f"{attraction}: No reviews found.")
