weather_system="weather_company";

today=$(date +'%Y-%m-%d');
dir_path=$(dirname $(readlink -f $0));
output="${dir_path}/Previsoes/${weather_system}_previsao_${today}.json";

parent_path="$(dirname ${dir_path})";
key=$(cat "${parent_path}/.API_keys/${weather_system}_API_key.txt");
# Precisa de cadastro / Requires registration
geocode="-22.955085,-43.071995";
# Usa coordenadas de latitude e longitude / uses latitude and longitude coordinates

curl -X GET -G "https://api.weather.com/v3/wx/forecast/daily/15day" -d "geocode=${geocode}" -d "units=m"  -d "language=pt-BR" -d "format=json" -d "apiKey=${key}" -H "accept: application/json" -o $output;
# Roda a cada dia / Runs every day
