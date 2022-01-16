import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope='playlist-modify-public'

username=input('Entrer votre user_id: ')

token = SpotifyOAuth(scope=scope,username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)

#creer playlist
playlist_name = input('Nom playlist: ')
playlist_desc = 'New songs from reddit'

spotifyObject.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_desc)

user_input = input('Enter the song: ')
list_songs = []
while user_input !='quit':
    result = spotifyObject.search(q=user_input)
    #print(json.dumps(result, sort_keys=4, indent=4))
    list_songs.append(result['tracks']['items'][0]['uri'])
    user_input = input('Enter the song: ')

prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']


spotifyObject.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=list_songs)

#/Users/jacobducas/Documents/GitHub/Reddit-music-Bot/spotifyApi.py