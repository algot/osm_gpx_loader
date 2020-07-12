import os
from colorama import init, Fore, Style

input_dir = 'input'


def upload(osm_helper):
    tracks_uploaded = 0

    files = _get_list_of_gpx_files(input_dir)

    for file in files:
        _print_color_text(80 * '-', Fore.YELLOW)
        print('Loading track: ' + file)
        current_loaded_track_id = osm_helper.post_gpx(
            osm_helper.session, os.path.join(input_dir, file))

        print('Track loaded')
        print('TrackId:', current_loaded_track_id)
        _print_color_text(80 * '-', Fore.YELLOW)
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


def _print_color_text(text, color):
    init(autoreset=True)
    print(color + Style.DIM + text)


def _print_summary(tracks_uploaded):
    init(autoreset=True)
    summary_text = (
        80 * '='
        + '\n'
        + 'SUMMARY:\n'
        + 'Tracks uploaded: '
        + str(tracks_uploaded)
        + '\n'
        + 80 * '='
    )
    _print_color_text(summary_text, Fore.GREEN)
