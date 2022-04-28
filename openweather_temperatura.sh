weather_system="openweather";

today=$(date +'%Y-%m-%d');
hour=$(date +'%H');
dir_path=$(dirname $(readlink -f $0));
output="${dir_path}/Temperaturas/${weather_system}_temperatura_${hour}_${today}.json";

parent_path="$(dirname ${dir_path})";
key=$(cat "${parent_path}/.API_keys/${weather_system}_API_key.txt");
# Precisa de cadastro / Requires registration at https://openweathermap.org/api

city="Niterói,BR";
# Usa Cidade,Código-do-País / Uses City/Country-code 


lat="-22.8832371";
lon="-43.1154552";

# curl -X GET -G "https://api.openweathermap.org/data/2.5/weather" -d "q=${city}" -d "appid=${key}" -d "units=metric" >> $output;
curl -X GET -G "https://api.openweathermap.org/data/2.5/onecall" -d "lat=${lat}" -d "lon=${lon}" -d "units=metric" -d "lang=pt_br" -d "exclude=minutely,hourly,daily,alerts" -d "appid=${key}" -H "Cache-Control: no-cache" -H "Accept: application/json" -o $output;
# Roda a cada hora, e adiciona a temperatura atual encontrada ao final do arquivo do dia 
# Runs every hour, appending the current temperature to day's file

