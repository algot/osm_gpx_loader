import requests
import os
from dotenv import load_dotenv

input_dir = 'input'


def get_session():
    load_dotenv()
    password = os.getenv('PASSWORD')
    user = os.getenv('USERNAME')
    session = requests.session()
    session.auth = (user, password)
    return session


def post_gpx(session, path_to_gpx_file):
    post_path = '/api/0.6/gpx/create'
    file_list = {'file': open(path_to_gpx_file, 'rb')}

    params = {'description': 'imported track', 'tags': 'import', 'visibility': 'trackable'}

    response_post = session.post(url=hostname + post_path, data=params, files=file_list)

    if response_post.status_code == 200:
        return response_post.text
    elif response_post.status_code == 401:
        raise ConnectionError('Authorization error (401)')
    elif response_post.status_code == 403:
        raise ConnectionError('Forbidden error (403)')
    else:
        raise ConnectionError('Error occured: ' + str(response_post.status_code))


def get_track_details(session, track_id):
    details_path = f'/api/0.6/gpx/{track_id}/details'
    response = session.get(hostname + details_path)
    content = response.content
    content = content.decode('utf8')
    print(content)


def get_list_of_gpx_files():
    filelist = os.listdir(input_dir)
    gpx_tracks = list(filter(lambda x: '.gpx' in x, filelist))
    return gpx_tracks


def print_list_of_files(filelist):
    print('Number of tracks: ' + str(len(filelist)))
    print('List of files in track directory: \n')
    print('\n'.join(filelist))


# hostname = 'https://master.apis.dev.openstreetmap.org'
hostname = 'https://api.openstreetmap.org'


current_session = get_session()

files = get_list_of_gpx_files()

tracks_uploaded = 0
for file in files:
    print('Loading track: ' + file)
    current_loaded_track_id = post_gpx(current_session, os.path.join(input_dir, file))

    print('track' + file + ' loaded')
    print('TrackId: ' + current_loaded_track_id)
    get_track_details(current_session, current_loaded_track_id)
    print(80 * '+')
    tracks_uploaded += 1

print(80 * '=')
print('SUMMARY:')
print('Tracks uploaded: ' + str(tracks_uploaded))
print(80 * '=')
