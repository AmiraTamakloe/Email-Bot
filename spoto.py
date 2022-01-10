import json

class CreatePlaylist:
    def __init__(self):
        pass
    def create_playlsit(self):
        request_body = json.dumps({
            "name": "Test_api",
            "description": "New playlist description",
            "public": True})
        
        query = 'https://api.spotify.com/v1/users/{user_id}/playlists'.format()
        
    def get_uri(self):
        pass
    def add_tracks(self):
        pass
