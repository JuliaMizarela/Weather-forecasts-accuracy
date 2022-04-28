weather_system="cptec_inpe";

today=$(date +'%Y-%m-%d');
file_name="${weather_system}_previsao_${today}.xml";
dir_path=$(dirname $(readlink -f $0));
output="${dir_path}/Previsoes/${file_name}";

city="3464";
# Pegar código da cidade em http://servicos.cptec.inpe.br/XML/ ou http://servicos.cptec.inpe.br/XML/listaCidades?city=nome da cidade

curl -X GET "servicos.cptec.inpe.br/XML/cidade/7dias/${city}/previsao.xml" -H "Accept: application/xml" -o $output;
php -q "${dir_path}/xml_to_json_converter.php" $output "${dir_path}/Previsoes/";
# Converte o XML para JSON com PHP / Converts the XMl response to JSON with PHP
rm $output;
# Roda a cada dia / Runs every day


