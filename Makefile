.ONESHELL:

FLASK_APP = src.weather.api
CITY_LIST_PATH = ./data/city.list.json

./.env: ./requirements.txt
	python3 -m venv .env
	. .env/bin/activate
	pip install -r requirements.txt

./.app_ready: ./.env
	. ./.env/bin/activate
	mkdir -p ./instance
	flask -A $(FLASK_APP) init-db
	flask -A $(FLASK_APP) load-city-list $(CITY_LIST_PATH)
	touch ./.app_ready

up_local: ./.app_ready
	. ./.env/bin/activate
	flask -A src.weather.api run

clean:
	rm -rf ./instance
	rm -rf ./.env
	rm -rf .app_ready
