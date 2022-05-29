# build containers
build:
	docker-compose -f docker-compose.yml build

# Run development containers
run-dev:
	docker-compose -f docker-compose.yml up db django-auth-template

# Run all containers in detached mode
run-dev-d:
	docker-compose -f docker-compose.yml up -d db django-auth-template

# Run database in detached mode
run-db:
	docker-compose -f docker-compose.yml up -d db

# Stop all containers
stop-all:
	docker-compose -f docker-compose.yml stop
	
# Attach app shell 
shell:
	docker-compose -f docker-compose.yml exec django-auth-template bash
	
# Create migration files
makemigrations:
	docker-compose -f docker-compose.yml exec django-auth-template pdm run makemigrations

# Merge migrations in case of conflict
mergemigration:
	docker-compose -f docker-compose.yml exec django-auth-template pdm run mergemigrations

# Apply migrations
migrate:
	docker-compose -f docker-compose.yml exec django-auth-template pdm run migrate

# Load setup data
loaddata:
	docker-compose -f docker-compose.yml exec django-auth-template pdm run loaddata 

# Dump database data
dumpdata:
	docker-compose -f docker-compose.yml exec django-auth-template pdm run dumpdata

# Run django tests
run-tests:
	docker-compose -f docker-compose.yml exec django-auth-template clear && date && make -f /home/python/app/Makefile test $(test) && date

# Removes all containers
remove-all:
	docker rm db django-auth-template-django

# Removes DB and db's data
remove-db:
	docker rm db && docker volume rm code_db_data

# Generate django static files
collectstatic:
	docker-compose -f docker-compose.yml exec django-auth-template pdm run collectstatic
