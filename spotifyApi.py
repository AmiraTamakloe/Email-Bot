import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json


scope='playlist-modify-public'
username='tctib79y7zvz39xim0jdvxcst'
oauth_object = spotipy.SpotifyOAuth(client_id='672c201896b64ca2afe2f1ead2b44f92', 
                                client_secret='93915893355a41928b818baf0de0f821',
                                redirect_uri='http://127.0.0.1:8080/',scope=scope)
token = oauth_object.get_access_token()


spotifyObject = spotipy.Spotify(auth=token['access_token'])

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