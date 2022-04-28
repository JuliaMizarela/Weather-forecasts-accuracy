weather_system="tiempo";

today=$(date +'%Y-%m-%d');
dir_path=$(dirname $(readlink -f $0));
output="${dir_path}/Previsoes/${weather_system}_previsao_${today}.json";

parent_path="$(dirname ${dir_path})";
key=$(cat "${parent_path}/.API_keys/${weather_system}_API_key.txt");
# Precisa de cadastro em / Requires registration at http://api.tiempo.com
city="115644";
# Pegar código da cidade em / Get city code at https://www.tiempo.com/api/#/panel/unaLocalidad

curl -X GET -G "http://api.tiempo.com/index.php" -d "api_lang=pt" -d "localidad=${city}" -d "affiliate_id=${key}" -d "v=3.0" -o $output;
# Retorna com um problema (irrelevante) de encoding de caracteres / Response has a (neglectable) char encoding issue
# Roda a cada dia / Runs every day
