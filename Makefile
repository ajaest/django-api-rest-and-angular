clean:
	rm -f example.sqlite

create_database:
	./env/bin/python ./manage.py makemigrations --noinput
	./env/bin/python ./manage.py migrate --noinput
	./env/bin/python ./manage.py createsuperuser --username=root --email=root@example.com --noinput
	chown apache:apache example.sqlite

make_fixtures:
	./env/bin/python ./manage.py create_users
	./env/bin/python ./manage.py create_posts
	./env/bin/python ./manage.py create_photos

make_scripts:
	grunt

all: make_scripts clean create_database make_fixtures
