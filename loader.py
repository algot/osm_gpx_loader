import requests
import os
from dotenv import load_dotenv


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

    params = {'description': 'desc', 'tags': 'tag', 'public': 1, 'visibility': 'public'}
    response_post = session.post(url=hostname + post_path, data=params, files=files)
    return response_post.text


def get_list_of_files():
    curr_dir = os.curdir
    file_list = os.listdir(curr_dir + '/input')
    print('Number of tracks: ' + str(len(file_list)))
    print('List of files in track directory: \n')
    print('\n'.join(file_list))




hostname = 'https://master.apis.dev.openstreetmap.org'

current_session = get_session()

track_loaded = post_gpx(current_session, os.curdir + '/input/1.gpx')
get_track_details(current_session, track_loaded)

get_list_of_files()
