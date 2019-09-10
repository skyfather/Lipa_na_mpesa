from mpesa import keys
# import keys
import requests
from requests.auth import HTTPBasicAuth
# from mpesa import keys

def generate_access_token():
    consumer_key = keys.consumer_key#"QtjogbhGY2J5wDb8y0fAR3RNHQWVOxJ5"#keys.consumer_key
    consumer_secret = keys.consumer_secret#"AcLg8RYpbpc7SBVd"#keys.consumer_secret
    api_URL = ("https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials")
    response = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key,consumer_secret))

    json_response = response.json()
    access_token = json_response['access_token']

    return access_token
