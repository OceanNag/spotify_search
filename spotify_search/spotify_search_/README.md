# spotify_search
Spotify Search
Spotify Search is a web application built with Flask that allows users to search for any artist on Spotify and view a dynamic artist homepage. Users can see an artist’s top tracks, popularity score, and profile picture—all in one place.
Features
Search for Artists – Find any artist by name using the Spotify API.
Artist Homepage – Displays:
Top songs of the artist
Spotify popularity score
Artist profile picture
Responsive Design – Works on both desktop and mobile devices.

Technologies Used
Backend: Python, Flask
Frontend: HTML, CSS
API: Spotify Web API via Spotipy
Environment Management: python-dotenv (dotenv)
Getting Started
Prerequisites
Python 3.x
Spotify Developer account with Client ID and Secret
Installation
Clone the repository:
git clone https://github.com/OceanNag/spotify_search.git
cd spotify-artist-explorer
Install dependencies:
pip install -r requirements.txt
Create a .env file and add your Spotify API credentials:
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
Run the Flask app:
python app.py
Usage
Enter the name of an artist in the search bar.
Click Search.
View the artist’s homepage with top tracks, popularity score, and profile image.
Future Improvements
Add album previews for top songs.
Include related artists suggestions.
Implement user login to save favorite artists.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request.