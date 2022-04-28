import json
import os
from pandas import to_datetime, Timestamp



###### OBJECTS
#      -------
#
dt_date_format = "%Y-%m-%d"
initial_date = "2022-04-22"
today = to_datetime("today").strftime(dt_date_format)


accuweather = "accuweather"
climatempo = "climatempo"
hgbrasil = "hgbrasil"
inmet = "inmet"
openweather = "openweather"
w_s_with_temperature = [accuweather, 
                        climatempo, 
                        hgbrasil, 
                        inmet, 
                        openweather]


cptec_inpe = "cptec_inpe"
tiempo = "tiempo"
weather_company = "weather_company"
w_s_with_forecast = [*w_s_with_temperature, 
                                cptec_inpe, 
                                tiempo, 
                                weather_company]

###### AUXILIARY FUNCTIONS
#      --------- ---------
#
def get_list_of_unique_dates(dir: str) -> list[str]:
    files_names = [file_name.name for file_name in os.scandir(dir) if file_name.is_file()]
    files_names_no_extension = [file_name.split(".")[:-1][0] for file_name in files_names]
    files_names_dates = [f_n_n_e.split("_")[-1:][0] for f_n_n_e in files_names_no_extension]
    unique_dates = [*set(files_names_dates)]
    unique_dates.sort()
    return unique_dates
    
def show_avaliable_forecast_dates() -> list[str]:
    print(f"Forecast made at: {get_list_of_unique_dates(r'../Previsoes/')}")

def show_avaliable_temperature_dates() -> list[str]:
    print(f"Forecast made at: {get_list_of_unique_dates(r'../Temperatura/')}")


###### TEMPERATURE FUNCTIONS
#      ----------- ---------
#

## Individual
#
def get_accuweather_temperature(accuweather_data):
    return accuweather_data[0]["Temperature"]["Metric"]["Value"]


def get_climatempo_temperature(climatempo_data):
    return climatempo_data["data"]["temperature"]


def get_hgbrasil_temperature(hgbrasil_data):
    return hgbrasil_data['temp']


def get_openweather_temperature(openweather_data):
    return openweather_data["current"]["temp"]


def get_inmet_temperature(inmet_data, hour: int):
    return inmet_data[hour]["TEM_INS"]


## Aggregators
#
def get_w_s_temperatures_at_date(w_s_string: str, date: str):
    hours_strings = [str(n).rjust(2,"0") for n in range(0, 24)]
    temperatures = []
    if w_s_string != "inmet":
        for hour in hours_strings:
            file_name = w_s_string + "_temperatura_"+hour+"_"+date+".json"
            with open(r'../Temperaturas/' + file_name, encoding="utf8") as data_file:
                w_s_data = json.load(data_file)
            function_name = "get_" + w_s_string + "_temperature"
            temperatures.append(globals()[function_name](w_s_data))
    else:
        file_name = w_s_string + "_temperatura_"+"23"+"_"+date+".json"
        with open(r'../Temperaturas/' + file_name, encoding="utf8") as data_file:
                w_s_data = json.load(data_file)
        _ = [temperatures.append(float(w_s_data[h]["TEM_INS"])) for h in range(0, len(w_s_data))]
    return {w_s_string: temperatures}

def aggregate_all_w_s_temperatures_at_date(date: str):
    agg_temperatures = {}
    agg_temperatures[date] = [get_w_s_temperatures_at_date(w_s_string, date) for w_s_string in w_s_with_temperature]
    print(date)
    for i in range(0, len(agg_temperatures[date])):
        for k, v in agg_temperatures[date][i].items():
            print(f"{k} - min: {min(v)}  max: {max(v)}")
    print("")

def aggregate_all_w_s_temperatures_at_all_dates():
    unique_temperatura_dates = get_list_of_unique_dates(r"../Temperaturas/")
    for date in unique_temperatura_dates:
        aggregate_all_w_s_temperatures_at_date(date)


###### FORECASTS FUNCTIONS
#      --------- ---------
#
unique_previsao_dates = get_list_of_unique_dates(r"../Previsoes/")

## Individual
#
def get_accuweather_forecast(accuweather_forecast_data):
    accuweather_forecast = {}
    for i in range(len(accuweather_forecast_data["DailyForecasts"])):
        date = to_datetime(accuweather_forecast_data["DailyForecasts"][i]["Date"]).strftime(dt_date_format)
        min = accuweather_forecast_data["DailyForecasts"][i]["Temperature"]["Minimum"]["Value"]
        max = accuweather_forecast_data["DailyForecasts"][i]["Temperature"]["Maximum"]["Value"]
        accuweather_forecast[date] = [min, max]
    return accuweather_forecast

def get_climatempo_forecast(climatempo_forecast_data):
    climatempo_forecast = {}
    for i in range(len(climatempo_forecast_data["data"])):
        date = to_datetime(climatempo_forecast_data["data"][i]["date"]).strftime(dt_date_format)
        min = climatempo_forecast_data["data"][i]["temperature"]["min"]
        max = climatempo_forecast_data["data"][i]["temperature"]["max"]
        climatempo_forecast[date] = [min, max]
    return climatempo_forecast

def get_hgbrasil_forecast(hgbrasil_forecast_data):
    hgbrasil_forecast = {}
    for i in range(len(hgbrasil_forecast_data["forecast"])):
        date = to_datetime("2022-"+hgbrasil_forecast_data["forecast"][i]["date"][3:]+"-"+hgbrasil_forecast_data["forecast"][i]["date"][:2]).strftime(dt_date_format)
        min = hgbrasil_forecast_data["forecast"][i]["min"]
        max = hgbrasil_forecast_data["forecast"][i]["max"]
        hgbrasil_forecast[date] = [min, max]
    return hgbrasil_forecast


def get_inmet_forecast(inmet_forecast_data):
    city = "3303302"
    inmet_forecast = {}
    for k in inmet_forecast_data[city].keys():
        date = k[6:] + "-" + k[3:5] + "-" + k[0:2]
        if "manha" in inmet_forecast_data[city][k].keys():
            mini = min(inmet_forecast_data[city][k]["manha"]["temp_min"], inmet_forecast_data[city][k]["tarde"]["temp_min"], inmet_forecast_data[city][k]["noite"]["temp_min"])
            maxi = max(inmet_forecast_data[city][k]["manha"]["temp_max"], inmet_forecast_data[city][k]["tarde"]["temp_max"], inmet_forecast_data[city][k]["noite"]["temp_max"])
        else:
            mini = inmet_forecast_data[city][k]["temp_min"]
            maxi = inmet_forecast_data[city][k]["temp_max"]
        inmet_forecast[date] = [mini, maxi]
    return inmet_forecast

def get_openweather_forecast(openweather_forecast_data):
    openweather_forecast = {}
    for i in range(len(openweather_forecast_data['daily'])):
        date = Timestamp(openweather_forecast_data['daily'][i]['dt'], unit='s').strftime(format=dt_date_format)
        min = openweather_forecast_data['daily'][i]['temp']['min']
        max = openweather_forecast_data['daily'][i]['temp']['max']
        openweather_forecast[date] = [min, max]
    return openweather_forecast

def get_cptec_inpe_forecast(cptec_inpe_forecast_data):
    cptec_inpe_forecast = {}
    for i in range(len(cptec_inpe_forecast_data['previsao'])):
        date = cptec_inpe_forecast_data['previsao'][i]['dia']
        min = cptec_inpe_forecast_data['previsao'][i]['minima']
        max = cptec_inpe_forecast_data['previsao'][i]['maxima']
        cptec_inpe_forecast[date] = [min, max]
    return cptec_inpe_forecast

def get_tiempo_forecast(tiempo_forecast_data):
    tiempo_forecast = {}
    for i in range(1, len(tiempo_forecast_data['day'])+1):
        date = tiempo_forecast_data['day'][str(i)]['date'][:4]+"-"+tiempo_forecast_data['day'][str(i)]['date'][4:6]+"-"+tiempo_forecast_data['day'][str(i)]['date'][6:]
        min = tiempo_forecast_data['day'][str(i)]['tempmin']
        max = tiempo_forecast_data['day'][str(i)]['tempmax']
        tiempo_forecast[date] = [min, max]
    return tiempo_forecast

def get_weather_company_forecast(weather_company_forecast_data):
    weather_company_forecast = {}
    for i in range(len(weather_company_forecast_data['calendarDayTemperatureMax'])):
        date = weather_company_forecast_data['sunriseTimeLocal'][i][:10]
        min = weather_company_forecast_data['calendarDayTemperatureMax'][i]
        max = weather_company_forecast_data['calendarDayTemperatureMin'][i]
        weather_company_forecast[date] = [min, max]
    return weather_company_forecast


## Aggregators
#
def get_w_s_forecast_made_at_date(w_s_string: str, date: str):
    forecast = {}
    file_name = w_s_string + "_previsao_"+date+".json"
    with open(r'../Previsoes/' + file_name, encoding="utf8") as data_forecast_file:
        w_s_forecast_data = json.load(data_forecast_file)
    function_name = "get_" + w_s_string + "_forecast"
    forecast[w_s_string] = globals()[function_name](w_s_forecast_data)
    return forecast

def get_all_forecasts_made_at_date(date):
    agg_forecast_made_at_date = [get_w_s_forecast_made_at_date(w_s_string, date) for w_s_string in w_s_with_forecast]
    return agg_forecast_made_at_date


