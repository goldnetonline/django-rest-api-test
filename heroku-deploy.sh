# git push heroku master
# touch /app/storage/logs/laravel.log
# cp /app/keys/* /app/storage/
# chmod -R 777 /app/storage/
# chmod -R 755 /app/modules/
touch /app/.env
python /app/manage.py migrate
#php /app/artisan migrate --force
#php /app/artisan package:discover
