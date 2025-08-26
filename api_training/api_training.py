# we use the following when using APIs
# CRUD = create, read, update and delete
# Create - post 
# Read - get
# update - put
# delete - delete

# We'll be learning REST - which is just standard use of reading data using API (rather than creating your own APIs)

import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv() #needed for the below - so we're not displaying all our secret API stuff in each py file, we'll keep it in a separate .env file

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

# API side

url = "https://accounts.spotify.com/api/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret

}

response = requests.post(url, headers = headers, data = data)
print("spotify_response - ", response)

access_token = response.json()["access_token"]

# artist_url = input("Enter the Spotify artist ID: ")




def search_by_artist(response, search_value):
    name = response.json()["artists"]["items"][0]["name"]
    if name == search_value:
        print("Artist Name - ",name)
    else: print("Did you mean",name,"?")
    url = response.json()['artists']["items"][0]["external_urls"]["spotify"]
    headers = {
    "Authorization": f"Bearer {access_token}"
}
    artist_url = url.split("/")[-1]
    artist_url = f"https://api.spotify.com/v1/artists/{artist_url}"
    artist_response = requests.get(artist_url, headers=  headers)
    print("Artist Name - ",name)
    print("Spotify Popularity - ",artist_response.json()["popularity"])
    print("Followers - ",response.json()["artists"]["items"][0]["followers"]["total"])

    print("Click here for more details",url)
    return ""



def search_by(search_type, search_value):
    assert search_type in ['artist', 'track', 'album', 'playlist']
    cleaned_search_value = search_value.replace(" ", "+")
    search_url = 'https://api.spotify.com/v1/search?q='+cleaned_search_value+'&type='+search_type
    headers = {
        "Authorization":f"Bearer {access_token}"
    }
    response = requests.get(search_url, headers = headers)
    search_type = search_type+'s'
    items = response.json()[search_type]["items"]
    print(items[0])
    if search_type == 'artists':
        print(search_by_artist(response, search_value))
    else: print("coming soon")


search_by("artist", "Kedghfick Lamar")