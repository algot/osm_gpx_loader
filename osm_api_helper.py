import requests


class OsmApiHelper:
    def __init__(self, env_settings):
        self.env_settings = env_settings
        auth_session = requests.session()
        auth_session.auth = (self.env_settings.username, self.env_settings.password)
        self.session = auth_session

    def post_gpx(self, path_to_gpx_file):
        post_path = '/api/0.6/gpx/create'
        file_list = {'file': open(path_to_gpx_file, 'rb')}

        params = {
            'description': 'imported track',
            'tags': 'import',
            'visibility': 'identifiable',
        }

        response_post = self.session.post(
            url=self.env_settings.hostname + post_path, data=params, files=file_list
        )

        if response_post.status_code == 200:
            return response_post.text
        elif response_post.status_code == 401:
            raise ConnectionError('Authorization error (401)')
        elif response_post.status_code == 403:
            raise ConnectionError('Forbidden error (403)')
        elif response_post.status_code == 503:
            raise ConnectionError(
                'Service Unavailable (503) \n' + response_post.content.decode('utf-8')
            )
        else:
            raise ConnectionError('Error occurred: ' + str(response_post.status_code))
