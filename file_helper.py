import os
from output_helper import print_color_text

input_dir = 'input'


def upload(osm_helper):
    tracks_uploaded = 0

    files = _get_list_of_gpx_files(input_dir)

    for file in files:
        print_color_text(80 * '-')
        print('Loading track: ' + file)
        current_loaded_track_id = osm_helper.post_gpx(os.path.join(input_dir, file))

        print('Track loaded')
        print('TrackId:', current_loaded_track_id)
        tracks_uploaded += 1

    return tracks_uploaded


def _get_list_of_gpx_files(input_dir):
    filelist = os.listdir(input_dir)
    gpx_tracks = list(filter(lambda x: '.gpx' in x, filelist))
    return gpx_tracks
