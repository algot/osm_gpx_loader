import requests
import os
from dotenv import load_dotenv

input_dir = '/input/'


def get_track_details(session, track_id):
    details_path = f'/api/0.6/gpx/{track_id}/details'
    response = session.get(hostname + details_path)
    content = response.content
    content = content.decode('utf8')
    print(content)


def get_session():
    load_dotenv()
    password = os.getenv('PASSWORD')
    user = os.getenv('USERNAME')
    session = requests.session()
    session.auth = (user, password)
    return session


def post_gpx(session, path_to_gpx_file):
    post_path = '/api/0.6/gpx/create'
    files = {'file': open(path_to_gpx_file, 'rb')}

    params = {'description': 'desc', 'tags': 'tag', 'visibility': 'trackable'}
    response_post = session.post(url=hostname + post_path, data=params, files=files)
    return response_post.text


def print_list_of_files(filelist):
    print('Number of tracks: ' + str(len(filelist)))
    print('List of files in track directory: \n')
    print('\n'.join(filelist))


def get_list_of_files():
    curr_dir = os.curdir
    return os.listdir(curr_dir + '/input')


hostname = 'https://master.apis.dev.openstreetmap.org'

current_session = get_session()

track_loaded_id = post_gpx(current_session, os.curdir + input_dir + '1.gpx')
get_track_details(current_session, track_loaded_id)

files = get_list_of_files()

for file in files:
    print('Loading track: ' + file)
    current_loaded_track_id = post_gpx(current_session, os.curdir + input_dir + file)
    print('track' + file + 'loaded')
    print('TrackId: ' + current_loaded_track_id)
    get_track_details(current_session, track_loaded_id)
    print('++++++++++++++++++++++++')
    pass
