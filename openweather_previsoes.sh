weather_system="openweather";

today=$(date +'%Y-%m-%d');
dir_path=$(dirname $(readlink -f $0));
output="${dir_path}/Previsoes/${weather_system}_previsao_${today}.json";

parent_path="$(dirname ${dir_path})";
key=$(cat "${parent_path}/.API_keys/${weather_system}_API_key.txt");
# Precisa de cadastro / Requires registration at https://openweathermap.org/api
city="Niterói,BR";
# Usa Cidade,Código-do-País / Uses City/Country-code 

lat="-22.8832371";
lon="-43.1154552";

# curl -X GET -G "https://api.openweathermap.org/data/2.5/forecast" -d "q=${city}" -d "appid=${key}" -d "units=metric" -d "cnt=5" -o $output;
curl -X GET -G "https://api.openweathermap.org/data/2.5/onecall" -d "lat=${lat}" -d "lon=${lon}" -d "units=metric" -d "lang=pt_br" -d "exclude=current,minutely,hourly,alerts" -d "appid=${key}" -H "Cache-Control: no-cache" -H "Accept: application/json" -o $output;
# Roda a cada dia / Runs every day

