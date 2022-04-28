weather_system="climatempo";

today=$(date +'%Y-%m-%d');
dir_path=$(dirname $(readlink -f $0));
output="${dir_path}/Previsoes/${weather_system}_previsao_${today}.json";

parent_path="$(dirname ${dir_path})";
key=$(cat "${parent_path}/.API_keys/${weather_system}_API_key.txt");
# Precisa de cadastro em https://www.climatempo.com.br/cadastro
city="6149";
# Pegar código de cidade em / Get city code at http://apiadvisor.climatempo.com.br/doc/index.html#api-Locale-GetCityByNameAndState Example: curl -i "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=São Paulo&state=SP&token=$key"
# Deve registrar a cidade à conta antes de usar a primeira vez / MUST also link the city to the token before first use:  curl -X PUT "http://apiadvisor.climatempo.com.br/api-manager/user-token/$key/locales" -H 'Content-Type: application/x-www-form-urlencoded' -d "localeId[]=$city";

curl -G "http://apiadvisor.climatempo.com.br/api/v2/forecast/locale/${city}/days/15" -d "token=${key}" -o $output;
# Roda a cada dia / Runs every day
# Opção de 15 dias é gratuita, a de 5 dias não... / The 15 days forecast is free, but not the 5 days one...
