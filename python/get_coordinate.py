import requests
import json
from parker_general import *

class GoogleMapHelper:
    api_key = None

    @classmethod
    def getApiKey(cls):
        if cls.api_key is None:
            with open(f"{repo_path}/auth/maps_api.key", 'r') as key_file:
                cls.api_key = key_file.readline().rstrip()
        return cls.api_key

    @classmethod
    def getCoordinate(cls, address):
        # Your Google API key
        _api_key = cls.getApiKey()
        
        # API endpoint URL
        url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={_api_key}'

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
    GoogleMapHelper.getCoordinate("承德路4段175號地下")