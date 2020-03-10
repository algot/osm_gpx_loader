import os
from dotenv import load_dotenv
import requests


class OsmApiHelper:

    def __init__(self):
        load_dotenv()
        self.hostname = os.getenv('HOSTNAME')
        self.username = os.getenv('USERNAME')
        self.password = os.getenv('PASSWORD')

        auth_session = requests.session()
        auth_session.auth = (self.username, self.password)
        self.session = auth_session

    def post_gpx(self, session, path_to_gpx_file):
        post_path = '/api/0.6/gpx/create'
        file_list = {'file': open(path_to_gpx_file, 'rb')}

        params = {'description': 'imported track',
                  'tags': 'import', 'visibility': 'trackable'}

        response_post = self.session.post(
            url=self.hostname + post_path, data=params, files=file_list)

        if response_post.status_code == 200:
            return response_post.text
        elif response_post.status_code == 401:
            raise ConnectionError('Authorization error (401)')
        elif response_post.status_code == 403:
            raise ConnectionError('Forbidden error (403)')
        else:
            raise ConnectionError('Error occurred: ' +
                                  str(response_post.status_code))

    def get_track_details(self, session, track_id):
        details_path = f'/api/0.6/gpx/{track_id}/details'
        response = session.get(self.hostname + details_path)
        content = response.content
        content = content.decode('utf8')
        print(content)
