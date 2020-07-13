from dotenv import load_dotenv
import os


class EnvSettings:
    def __init__(self):
        load_dotenv()
        self.hostname = os.getenv('OSM_HOSTNAME')
        self.username = os.getenv('OSM_USERNAME')
        self.password = os.getenv('OSM_PASSWORD')
