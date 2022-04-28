weather_system="accuweather";

today=$(date +'%Y-%m-%d');
hour=$(date +'%H');
dir_path=$(dirname $(readlink -f $0));
output="${dir_path}/Temperaturas/${weather_system}_temperatura_${hour}_${today}.json";

parent_path="$(dirname ${dir_path})";
key=$(cat "${parent_path}/.API_keys/${weather_system}_API_key.txt");
# Precisa de cadastro em / Requires registration at https://developer.accuweather.com/
city="2729531";
# Pegar código da cidade em / Get city code at https://developer.accuweather.com/accuweather-locations-api/apis

curl -X GET -G "http://dataservice.accuweather.com/currentconditions/v1/${city}" -d "apikey=${key}" -d "language=pt-BR" -H "Cache-Control: no-cache" >> $output;
# Roda a cada hora, e adiciona a temperatura atual encontrada ao final do arquivo do dia 
# Runs every hour, appending the current temperature to day's file
