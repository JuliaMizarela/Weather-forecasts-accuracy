weather_system="inmet";

today=$(date +'%Y-%m-%d');
hour=$(date +'%H');
dir_path=$(dirname $(readlink -f $0));
output="${dir_path}/Temperaturas/${weather_system}_temperatura_${hour}_${today}.json";

station="A627";
# Pegar código da estação em https://apiprevmet3.inmet.gov.br/estacao/proxima/3303302 sendo o numero o geocode da cidade
# Pegar o geocode da cidade em https://servicodados.ibge.gov.br/api/docs/localidade

curl "https://apitempo.inmet.gov.br/estacao/${today}/${today}/${station}" -o $output;
# Roda a cada dia pegando todas as temperaturas do dia
