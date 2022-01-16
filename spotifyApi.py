import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json


username='amiratk11'

#auth
scope='playlist-modify-public'
oauth_object = spotipy.SpotifyOAuth(client_id='672c201896b64ca2afe2f1ead2b44f92', 
                                client_secret='93915893355a41928b818baf0de0f821',
                                redirect_uri='http://127.0.0.1:8080/',scope=scope)
token = oauth_object.get_access_token()
spotifyObject = spotipy.Spotify(auth=token['access_token'])

def create_playlist():
#creer playlist
    playlist_name = input('Nom playlist: ')
    playlist_desc = input("Your playlist's description: ")

    spotifyObject.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_desc)
def reddit_songs():
    pass

def add_songs():
    #add specifics songs
    etat = True
    state = True
    list_songs = []
    while state == True:
        rep = input("Do you want to add a specific song?(y/n): ")

        if rep == 'y':
            user_input = input('Enter the title: ')
            while user_input != 'quit':
                result = spotifyObject.search(q=user_input)
                #print(json.dumps(result, sort_keys=4, indent=4))
                list_songs.append(result['tracks']['items'][0]['uri'])
                user_input = input('Enter the title (TYPE QUIT TO STOP): ')
            state = False

        elif rep == 'n':
            state = False

        else:
            print('Incorrect input!')
    #add reddit songs
    while etat == True:
        rep = input('Do you want to add songs found by our Reddit bot (y/n)?: ')

        if rep == 'y':
            #à modifier pour accomoder le query
            rs = reddit_songs()
            #list_songs.extend(rs)
        elif rep == "n":
            etat = False

        else:
            print('Incorrect input!')
    
    return list_songs

def main():
    create_playlist()
    prePlaylist = spotifyObject.user_playlists(user=username)
    playlist = prePlaylist['items'][0]['id']

    chansons = add_songs()

    spotifyObject.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=chansons)

if __name__=='__main__':
    main()



    