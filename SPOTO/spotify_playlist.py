import json
import os
import csv
import requests
from refresh import Refresh

from secrets import spotify_token, spotify_user_id

class CreatePlaylist:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token =spotify_token
        self.tracks = ""
        self.new_playlist_id = ""

    def avoir_chansons(self):
        songs = []
        with open('Single.csv', 'r') as f:
            reader= csv.reader(f)
            for row in reader:
                songs.append(row[2])

        for i in songs:
            self.tracks += i
        self.tracks = self.tracks[:-1]

        self.add_tracks()

    def create_playlist(self):
        request_body = json.dumps({
            "name": "Test_api",
            "description": "New playlist description",
            "public": True})
        
        query = 'https://api.spotify.com/v1/users/{user_id}/playlists'.format(self.user_id)
        response = requests.post(
            query,
            data=request_body,
            headers={
                'Content-type':"application/json",
                "Authorization":"Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        #playlist id
        return response_json['id']

    def add_tracks(self):
        #faire un dict
        self.playlist_id = self.create_playlist()

        query = "https://api.spotify.com/v1/playlists/{}/tracks?uris={}".format(self.playlist_id, self.tracks)

        response = requests.post(query, headers={"Content-Type": "application/json",
                                                 "Authorization": "Bearer {}".format(self.spotify_token)})

        print(response.json)


    def call_refresh(self):

        print("Refreshing token")

        refreshCaller = Refresh()

        self.spotify_token = refreshCaller.refresh()

        self.avoir_chansons()


a = CreatePlaylist()
a.call_refresh()
