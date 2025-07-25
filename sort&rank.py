import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Step 1: Authenticate - ID si username & secret is pswd
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="user-top-read playlist-modify-public",
    redirect_uri="http://localhost:8888/callback",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET"
))

# Step 2: Get top tracks from the past month
top_tracks = sp.current_user_top_tracks(limit=20, time_range='short_term')

# Step 3: Rank tracks by popularity
ranked_tracks = sorted(top_tracks['items'], key=lambda x: x['popularity'], reverse=True)

# Step 4: Create a new playlist
user_id = sp.me()['id']
playlist = sp.user_playlist_create(
    user=user_id,
    name="Songs your friends should listen to or...maybe not",
    public=True,
    description="A collection of my most repeated tracks this month. Judge me if you must."
)

# Step 5: Add tracks to the playlist
track_uris = [track['uri'] for track in ranked_tracks]
sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)

print("Playlist created successfully!")
