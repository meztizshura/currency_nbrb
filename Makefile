up:
	docker compose up -d

build:
	docker compose build

down:
	docker compose down

up-dev:
	docker compose up

req:
	docker compose exec web sh mnt/extra-addons/collect_requirements.sh

restart:
	docker compose restart web

upd:
	docker compose run web -d $(db) -u $(module)
	docker compose restart
