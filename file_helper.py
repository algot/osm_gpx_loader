import os

input_dir = 'input'


def upload(osm_helper):
    tracks_uploaded = 0

    files = _get_list_of_gpx_files(input_dir)

    for file in files:
        _print_yellow_text(80 * '-')
        print('Loading track: ' + file)
        current_loaded_track_id = osm_helper.post_gpx(
            osm_helper.session, os.path.join(input_dir, file))

        print('Track loaded')
        print('TrackId:', current_loaded_track_id)
        _print_yellow_text(80 * '-')
        tracks_uploaded += 1

    _print_summary(tracks_uploaded)

def _get_list_of_gpx_files(input_dir):
    filelist = os.listdir(input_dir)
    gpx_tracks = list(filter(lambda x: '.gpx' in x, filelist))
    return gpx_tracks

def _print_list_of_files(filelist):
    print('Number of tracks: ' + str(len(filelist)))
    print('List of files in track directory: \n')
    print('\n'.join(filelist))

def _print_yellow_text(text):
    print('\033[33m{}\033[0m'.format(text))

def _make_green(func):
    def wrapper(*args, **kwargs):
        print('\033[32m')
        func(*args, **kwargs)
        print('\033[0m')

    return wrapper

@_make_green
def _print_summary(tracks_uploaded):
    print(80 * '=')
    print('SUMMARY:')
    print('Tracks uploaded: ' + str(tracks_uploaded))
    print(80 * '=')
