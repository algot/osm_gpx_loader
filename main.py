from env_settings import EnvSettings
import osm_api_helper
import file_helper
import output_helper


def main():
    env_settings = EnvSettings()
    osm_helper = osm_api_helper.OsmApiHelper(env_settings)

    output_helper.print_header(env_settings)
    tracks_uploaded = file_helper.upload(osm_helper)
    output_helper.print_summary(tracks_uploaded)


if __name__ == '__main__':
    main()
