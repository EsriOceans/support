import requests  # pip install requests

def get_token():
    params = {
        'client_id': "YOUR_APPLICATIONS_CLIENT_ID",
        'client_secret': "YOUR_APPLICATIONS_CLIENT_SECRET",
        'grant_type': "client_credentials"
    }

    request = requests.get('https://www.arcgis.com/sharing/oauth2/token',
                           params=params)
    response = request.json()
    token = response["access_token"]
    return token

token = get_token()
print(token)
