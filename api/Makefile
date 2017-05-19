JULY_APP_LIST=article category tag user comment july
JULY_DB_FILE=db.sqlite3

.PHONY: all migrate clean start


all:
	@echo [clean] up migrations and database file
	@echo [migrate] database
	@echo [start] server


migrate:
	python manage.py makemigrations $(JULY_APP_LIST)
	python manage.py migrate


clean:
	rm -rf */migrations
	@if [ -f $(JULY_DB_FILE) ]; then \
		rm -f $(JULY_DB_FILE); \
	fi


start:
	python manage.py runserver 127.0.0.1:9999


