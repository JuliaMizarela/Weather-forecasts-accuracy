weather_system="inmet";

today=$(date +'%Y-%m-%d');
dir_path=$(dirname $(readlink -f $0));
output="${dir_path}/Previsoes/${weather_system}_previsao_${today}.json";

city="3303302";
# Pegar o geocode da cidade em https://servicodados.ibge.gov.br/api/docs/localidade

curl "https://apiprevmet3.inmet.gov.br/previsao/${city}" -o $output;
# Roda a cada dia / Runs every day
