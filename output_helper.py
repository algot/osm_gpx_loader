from colorama import init, Fore, Style


def print_header(env_settings):
    print(' OSM GPX LOADER '.center(80, '='))
    print_bright_text(env_settings.hostname.upper().center(80))


def print_summary(tracks_uploaded):
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
    print_color_text(summary_text, Fore.GREEN)


def print_color_text(text, color=Fore.YELLOW):
    init(autoreset=True)
    print(color + Style.DIM + text)


def print_bright_text(text):
    init(autoreset=True)
    print(Style.BRIGHT + text)


def _print_list_of_files(filelist):
    print('Number of tracks: ' + str(len(filelist)))
    print('List of files in track directory: \n')
    print('\n'.join(filelist))
