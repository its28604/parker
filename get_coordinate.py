import requests
import json

def getCoordinate(address):
    # Your Google API key
    api_key = 'AIzaSyCytHMblMygk9UlGZpgkwB_B1eCnCnFdNg'

    # API endpoint URL
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'

    # Sending a request to the API
    response = requests.get(url)

    # Parsing the response to JSON
    data = response.json()

    coor = ""
    # Extracting latitude and longitude
    if data['status'] == 'OK':
        latitude = data['results'][0]['geometry']['location']['lat']
        longitude = data['results'][0]['geometry']['location']['lng']
        # print(f'Latitude: {latitude}, Longitude: {longitude}')
        coor = f'{latitude}, {longitude}'
    else:
        print('Error or no results found')
    return coor

if __name__ == "__main__":
    getCoordinate("承德路4段175號地下")