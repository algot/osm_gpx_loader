import osm_api_helper
import file_helper


def main():
    osm_helper = osm_api_helper.OsmApiHelper()
    file_helper.upload(osm_helper)


if __name__ == '__main__':
    main()
