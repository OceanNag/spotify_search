from flask import Flask, request, render_template
import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import spotify_functions

from flask_sqlalchemy import SQLAlchemy # if this comes up as an error message, do source .venv/bin/activate

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

load_dotenv()

@app.route("/")
@app.route("/index")
def index():
    return render_template(
        "index.html"
    )

def top_track_details(top_tracks_json:dict, number:int)->dict:
    return {
        "title":top_tracks_json["tracks"][number]["name"],
        "url":top_tracks_json["tracks"][number]["external_urls"]["spotify"],
        "album":top_tracks_json["tracks"][number]["album"]["name"],
        "spotify_rating":top_tracks_json["tracks"][number]["popularity"]
    }


@app.route("/artists")
def artist_home():
    artist_query = request.args.get('artist')
    result = spotify_functions.search_by_artist(artist_query)
    def normalise_name(name):
        return name.replace(".","").lower()
    if normalise_name(result['name']) != normalise_name(artist_query):
        return render_template(
            "not_found.html", 
            suggested_name = result['name']
        )
    api_id = result['id']
    top_tracks_data = spotify_functions.get_artists_top_tracks(api_id)
    if result["genres"] == []:
        genre_list = ""
    else:
        genre_list = result["genres"][0]

    return render_template(
            "spotify.html",
            title = result['name'],
            popularity = result['popularity'],
            spotify_url = result['external_urls']['spotify'],
            genre = genre_list,
            id = api_id,
            artist_image = result["images"][0]["url"],
            top_tracks = top_track_details(top_tracks_data, 0),
            top_tracks_2 = top_track_details(top_tracks_data, 1),
            top_tracks_3 = top_track_details(top_tracks_data, 2),
            top_tracks_4 = top_track_details(top_tracks_data, 3),
            top_tracks_5 = top_track_details(top_tracks_data, 4),
            json_items = result,
        )

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000)

# look into waitress