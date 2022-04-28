weather_system="climatempo";

today=$(date +'%Y-%m-%d');
hour=$(date +'%H');
dir_path=$(dirname $(readlink -f $0));
output="${dir_path}/Temperaturas/${weather_system}_temperatura_${hour}_${today}.json";

parent_path="$(dirname ${dir_path})";
key=$(cat "${parent_path}/.API_keys/${weather_system}_API_key.txt");
# Precisa de cadastro em https://www.climatempo.com.br/cadastro
city="6149";
# Pegar código de cidade em / Get city code at http://apiadvisor.climatempo.com.br/doc/index.html#api-Locale-GetCityByNameAndState Example: curl -i "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=São Paulo&state=SP&token=$key"
# Deve registrar a cidade à conta antes de usar a primeira vez / MUST also link the city to the token before first use:  curl -X PUT "http://apiadvisor.climatempo.com.br/api-manager/user-token/$key/locales" -H 'Content-Type: application/x-www-form-urlencoded' -d "localeId[]=$city";

curl -G "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/${city}/current" -d "token=${key}" >> $output;
# Roda a cada hora, e adiciona a temperatura atual encontrada ao final do arquivo do dia 
# Runs every hour, appending the current temperature to day's file
