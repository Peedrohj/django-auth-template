# build containers
build:
	docker-compose build

# Run development containers
run-dev:
	docker-compose up db django-auth-template

# Run all containers in detached mode
run-dev-d:
	docker-compose up -d db django-auth-template

# Run database in detached mode
run-db:
	docker-compose up -d db

# Stop all containers
stop-all:
	docker-compose stop
	
# Attach app shell 
shell:
	docker-compose exec django-auth-template bash
	
# Create migration files
makemigrations:
	docker-compose exec django-auth-template pdm run code/manage.py makemigrations

# Merge migrations in case of conflict
mergemigration:
	docker-compose exec django-auth-template pdm run code/manage.py makemigrations --merge

# Apply migrations
migrate:
	docker-compose exec django-auth-template pdm run code/manage.py migrate

# Load setup data
loaddata:
	docker-compose exec django-auth-template pdm run code/manage.py loaddata fixtures/setup-dump.json

# Dump database data
dumpdata:
	docker-compose exec django-auth-template pdm run code/manage.py dumpdata --natural-foreign --natural-primary -e sessions -e admin.logentry -e core.logactionmodel --indent 4 > fixtures/setup-dump.json

# Run django tests
run-tests:
	docker-compose exec django-auth-template clear && date && pdm run code/manage.py test $(test) && date

# Removes all containers
remove-all:
	docker rm db django-auth-template-django

# Removes DB and db's data
remove-db:
	docker rm db && docker volume rm code_db_data

# Generate django static files
collectstatic:
	docker-compose exec django-auth-template pdm run code/manage.py collectstatic
