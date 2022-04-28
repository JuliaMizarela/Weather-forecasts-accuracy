weather_system="accuweather";

today=$(date +'%Y-%m-%d');
dir_path="$(dirname "$(readlink -fm "$0")")";
output="${dir_path}/Previsoes/${weather_system}_previsao_${today}.json";

parent_path="$(dirname ${dir_path})";
key=$(cat "${parent_path}/.API_keys/${weather_system}_API_key.txt");
# Precisa de cadastro em / Requires registration at https://developer.accuweather.com/
city="2729531";
# Pegar código da cidade em / Get city code at https://developer.accuweather.com/accuweather-locations-api/apis

curl -X GET -G "http://dataservice.accuweather.com/forecasts/v1/daily/5day/${city}" -d "apikey=${key}" -d "language=pt-BR" -d "metric=true" -H "Cache-Control: no-cache" -o $output;
# Roda a cada dia / Runs every day
