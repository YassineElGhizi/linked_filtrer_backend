if [[ $CREATE_SUPERUSER ]];
then
  python manage.py migrate --noinput
  python manage.py collectstatic --noinput
  python manage.py migrate auth
#  python manage.py createsuperuser --no-input
fi