echo "Applying migrations"
python ./manage.py migrate
echo "Collecting static files"
python ./manage.py collectstatic --clear --noinput
echo "Starting server"
python ./manage.py runserver 0.0.0.0:8000