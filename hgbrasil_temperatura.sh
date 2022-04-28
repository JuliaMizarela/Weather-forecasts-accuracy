weather_system="hgbrasil";

today=$(date +'%Y-%m-%d');
hour=$(date +'%H');
dir_path=$(dirname $(readlink -f $0));
output="${dir_path}/Temperaturas/${weather_system}_temperatura_${hour}_${today}.json";

parent_path="$(dirname ${dir_path})";
key=$(cat "${parent_path}/.API_keys/${weather_system}_API_key.txt");
# Precisa de cadastro (tem versão simplificada sem cadastro) em https://hgbrasil.com/

city="455891";
# Codigo de cidade em https://console.hgbrasil.com/documentation/weather/tools

curl -X GET -G "https://api.hgbrasil.com/weather" -d "woeid=${city}" -d "format=json" -d "fields=only_results,city_name,temp,date,time" -d "key=${key}" -H "Cache-control: no-cache" >> $output;
