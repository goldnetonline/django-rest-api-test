parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
date=$(date +%s)
dateEnv="ASSET_VERSION=$date"
echo $dateEnv >> .env

# Robots.txt writer
printf "${!APP_ENV}"
echo $APP_ENV;

if [ $APP_ENV != 'production' ]
    then
    echo "This is not production environment, writing robots.txt";
    printf 'User-Agent: *\nDisallow: /\n' > robots.txt

fi;