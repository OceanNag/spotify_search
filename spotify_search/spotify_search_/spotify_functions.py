from flask import Flask, request
import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

from flask_sqlalchemy import SQLAlchemy # if this comes up as an error message, do source .venv/bin/activate

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Spotify_artist_data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), unique = True, nullable = False)
    followers = db.Column(db.Integer)
    popularity = db.Column(db.Integer)
    spotify_url = db.String(120)

    def extract_relevant_data(self):
        return {
            "id":self.id,
            "name":self.name,
            "followers":self.followers,
            "popularity":self.popularity,
            "spotify_url":self.spotify_url
        }
with app.app_context():
    db.create_all()

load_dotenv()

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

# TODO we need to amend the below to be more 'return' esque, rather than print statements. 

# region spotify_functions

def search_by_artist(search_value):
    cleaned_search_value = search_value.replace(" ", "+")
    
    search_url = f'https://api.spotify.com/v1/search?q={cleaned_search_value}&type=artist'
    headers = {"Authorization": f"Bearer {access_token}"}
    
    response = requests.get(search_url, headers=headers)
    data = response.json()

    # Get first artist item (if exists)
    items = data["artists"]["items"]
    if not items:
        return None  # No artist found
    
    artist = items[0]
    return artist


def get_artists_top_tracks(id):
    headers = {"Authorization": f"Bearer {access_token}"}
    print(headers)
    artist_url = f"https://api.spotify.com/v1/artists/{id}/top-tracks"
    response = requests.get(artist_url, headers=headers)
    data = response.json()

    return data

# endregion



@app.route("/")
def index():
    return "Ocean app homepage"

@app.route("/artists")
def artist_home():
    return "Artist homepage"



if __name__ == "__main__":
    print('\n Get Spotify Artist Data \n')

    artist = input("Please enter Artist Name")