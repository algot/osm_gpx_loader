# OSM GPX UPLOADER

## Installation
* Clone repository - `git clone https://github.com/algot/osm_gpx_loader.git`
* Navigate to directory - `cd osm_gpx_loader`
* Create environment settings file - `cp .env.example .env `
* Specify username/password in `.env`
* Comment or remove unnecessary hostname (# for comment) - 
  * production 'https://api.openstreetmap.org'
  * test 'https://master.apis.dev.openstreetmap.org'
* Install **pipenv** - `sudo apt install pipenv`
* Create **pipenv** environment - `pipenv shell`
* Update dependencies - `pipenv sync`

## Usage
* Put all *.gpx tracks inside 'input' directory
* Navigate to **osm_gpx_loader** directory
* Open pipenv shell - `pipenv shell`
* Update dependencies - `pipenv sync`
* Run `python main.py`