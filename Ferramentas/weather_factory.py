from weather_classes import *
import os
import json
import pandas as pd
from itertools import chain
from pandas import to_datetime, Timestamp



###### OBJECTS
#      -------
#
accuweather = Weather_system("accuweather")
climatempo = Weather_system("climatempo")
hgbrasil = Weather_system("hgbrasil")
inmet = Weather_system("inmet")
openweather = Weather_system("openweather")
w_s_with_temperature = [accuweather, 
                        climatempo, 
                        hgbrasil, 
                        inmet, 
                        openweather]


cptec_inpe = Weather_system("cptec_inpe")
tiempo = Weather_system("tiempo")
weather_company = Weather_system("weather_company")
w_s_with_forecast = [*w_s_with_temperature, 
                                cptec_inpe, 
                                tiempo, 
                                weather_company]


dt_date_format = "%Y-%m-%d"
initial_date = "2022-04-22"
today = to_datetime("today").strftime(dt_date_format)


###### AUXILIARY FUNCTIONS
#      --------- ---------
#
def get_list_of_unique_dates(dir: str) -> list[str]:
    """
    Checks file names in dir for unique %Y%M%d, following the naming convention: 
    weather_system_name + _previsao_ + %Y%M%d + .json   -> when forecast
    weather_system_name + _temperatura_ + %Y%M%d + .json   -> when daily temperature
    """
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




## Aggregated
#
def create_w_s_current_temperatures_at_date(w_s: Weather_system, date: str) -> list:
    hours_strings = [str(n).rjust(2,"0") for n in range(0, 24)]
    current_temperatures = []
    function_name = "get_" + repr(w_s) + "_temperature"
    if w_s != inmet:
        for hour in hours_strings:
            file_name = repr(w_s) + "_temperatura_"+hour+"_"+date+".json"
            with open(r'../Temperaturas/' + file_name, encoding="utf8") as data_file:
                w_s_data = json.load(data_file)
            current_temperatures.append(Current_temperature(w_s, date, Temperature(globals()[function_name](w_s_data)), hour))
    else:
        file_name = repr(w_s) + "_temperatura_"+"23"+"_"+date+".json"
        with open(r'../Temperaturas/' + file_name, encoding="utf8") as data_file:
                w_s_data = json.load(data_file)
        for h in range(0, len(w_s_data)):
            current_temperatures.append(Current_temperature(w_s, date, Temperature(globals()[function_name](w_s_data, h)), hours_strings[h]))
    return current_temperatures

def create_all_w_s_temperatures_at_all_dates():
    unique_temperatura_dates = get_list_of_unique_dates(r"../Temperaturas/")
    all_temperatures = []
    for date in unique_temperatura_dates:
        for w_s in w_s_with_temperature:
            all_temperatures.append(create_w_s_current_temperatures_at_date(w_s, date))
    return all_temperatures



###### FORECASTS FUNCTIONS
#      --------- ---------
#
## Individual
#
def create_accuweather_forecast(accuweather_forecast_data, at_date):
    pass
    accuweather_forecasts = []
    for i in range(len(accuweather_forecast_data["DailyForecasts"])):
        date = to_datetime(accuweather_forecast_data["DailyForecasts"][i]["Date"]).strftime(dt_date_format)
        min = Temperature(accuweather_forecast_data["DailyForecasts"][i]["Temperature"]["Minimum"]["Value"])
        max = Temperature(accuweather_forecast_data["DailyForecasts"][i]["Temperature"]["Maximum"]["Value"])
        accuweather_forecasts.append(Daily_forecast(accuweather, at_date, Temperature_range(min, max), date))
    return accuweather_forecasts

def create_climatempo_forecast(climatempo_forecast_data, at_date):
    climatempo_forecasts = []
    for i in range(len(climatempo_forecast_data["data"])):
        date = to_datetime(climatempo_forecast_data["data"][i]["date"]).strftime(dt_date_format)
        min = Temperature(climatempo_forecast_data["data"][i]["temperature"]["min"])
        max = Temperature(climatempo_forecast_data["data"][i]["temperature"]["max"])
        climatempo_forecasts.append(Daily_forecast(climatempo, at_date, Temperature_range(min, max), date))
    return climatempo_forecasts

def create_hgbrasil_forecast(hgbrasil_forecast_data, at_date):
    hgbrasil_forecasts = []
    for i in range(len(hgbrasil_forecast_data["forecast"])):
        date = to_datetime("2022-"+hgbrasil_forecast_data["forecast"][i]["date"][3:]+"-"+hgbrasil_forecast_data["forecast"][i]["date"][:2]).strftime(dt_date_format)
        min = Temperature(hgbrasil_forecast_data["forecast"][i]["min"])
        max = Temperature(hgbrasil_forecast_data["forecast"][i]["max"])
        hgbrasil_forecasts.append(Daily_forecast(hgbrasil, at_date, Temperature_range(min, max), date))
    return hgbrasil_forecasts

def create_inmet_forecast(inmet_forecast_data, at_date):
    city = "3303302"
    inmet_forecasts = []
    for k in inmet_forecast_data[city].keys():
        date = k[6:] + "-" + k[3:5] + "-" + k[0:2]
        if "manha" in inmet_forecast_data[city][k].keys():
            mini = Temperature(min(inmet_forecast_data[city][k]["manha"]["temp_min"], inmet_forecast_data[city][k]["tarde"]["temp_min"], inmet_forecast_data[city][k]["noite"]["temp_min"]))
            maxi = Temperature(max(inmet_forecast_data[city][k]["manha"]["temp_max"], inmet_forecast_data[city][k]["tarde"]["temp_max"], inmet_forecast_data[city][k]["noite"]["temp_max"]))
        else:
            mini = Temperature(inmet_forecast_data[city][k]["temp_min"])
            maxi = Temperature(inmet_forecast_data[city][k]["temp_max"])
        inmet_forecasts.append(Daily_forecast(inmet, at_date, Temperature_range(mini, maxi), date))
    return inmet_forecasts

def create_openweather_forecast(openweather_forecast_data, at_date):
    openweather_forecasts = []
    for i in range(len(openweather_forecast_data['daily'])):
        date = Timestamp(openweather_forecast_data['daily'][i]['dt'], unit='s').strftime(format=dt_date_format)
        min = Temperature(openweather_forecast_data['daily'][i]['temp']['min'])
        max = Temperature(openweather_forecast_data['daily'][i]['temp']['max'])
        openweather_forecasts.append(Daily_forecast(openweather, at_date, Temperature_range(min, max), date))
    return openweather_forecasts

def create_cptec_inpe_forecast(cptec_inpe_forecast_data, at_date):
    cptec_inpe_forecasts = []
    for i in range(len(cptec_inpe_forecast_data['previsao'])):
        date = cptec_inpe_forecast_data['previsao'][i]['dia']
        min = Temperature(cptec_inpe_forecast_data['previsao'][i]['minima'])
        max = Temperature(cptec_inpe_forecast_data['previsao'][i]['maxima'])
        cptec_inpe_forecasts.append(Daily_forecast(cptec_inpe, at_date, Temperature_range(min, max), date))
    return cptec_inpe_forecasts

def create_tiempo_forecast(tiempo_forecast_data, at_date):
    tiempo_forecasts = []
    for i in range(1, len(tiempo_forecast_data['day'])+1):
        date = tiempo_forecast_data['day'][str(i)]['date'][:4]+"-"+tiempo_forecast_data['day'][str(i)]['date'][4:6]+"-"+tiempo_forecast_data['day'][str(i)]['date'][6:]
        min = Temperature(tiempo_forecast_data['day'][str(i)]['tempmin'])
        max = Temperature(tiempo_forecast_data['day'][str(i)]['tempmax'])
        tiempo_forecasts.append(Daily_forecast(tiempo, at_date, Temperature_range(min, max), date))
    return tiempo_forecasts


## Aggregated
#
def create_weather_company_forecast(weather_company_forecast_data, at_date):
    weather_company_forecasts = []
    for i in range(len(weather_company_forecast_data['calendarDayTemperatureMax'])):
        date = weather_company_forecast_data['sunriseTimeLocal'][i][:10]
        min = Temperature(weather_company_forecast_data['calendarDayTemperatureMax'][i])
        max = Temperature(weather_company_forecast_data['calendarDayTemperatureMin'][i])
        weather_company_forecasts.append(Daily_forecast(weather_company, at_date, Temperature_range(min, max), date))
    return weather_company_forecasts

def create_forecasts_made_at_date(w_s: Weather_system, date: str):
    daily_forecasts = []
    file_name = repr(w_s) + "_previsao_"+date+".json"
    with open(r'../Previsoes/' + file_name, encoding="utf8") as data_forecast_file:
        w_s_forecast_data = json.load(data_forecast_file)
    function_name = "create_" + repr(w_s) + "_forecast"
    daily_forecasts.append(globals()[function_name](w_s_forecast_data, date))
    return daily_forecasts

def create_all_forecasts_made_at_date(date):
    agg_forecast_made_at_date = []
    for w_s in w_s_with_forecast:
        agg_forecast_made_at_date.append(create_forecasts_made_at_date(w_s, date))
    return agg_forecast_made_at_date

def create_all_forecasts_made_at_all_dates():
    unique_previsao_dates = get_list_of_unique_dates(r'../Previsoes/')
    agg_forecasts_made_at_all_dates = []
    for date in unique_previsao_dates:
        agg_forecasts_made_at_all_dates.append(create_all_forecasts_made_at_date(date))
    return agg_forecasts_made_at_all_dates



df = pd.DataFrame([ct.__dict__() for ct in chain(*create_all_w_s_temperatures_at_all_dates())])
print(df.groupby(["date_of_measurement", "weather_system"]).agg(Min=('temperature', 'min'), Max=('temperature', 'max')))


# print(create_all_forecasts_made_at_all_dates())
df2 = pd.DataFrame([ct.__dict__() for ct in chain(*chain(*chain(*create_all_forecasts_made_at_all_dates())))])
for w_s in w_s_with_forecast:
    df2a = df2[df2.weather_system == w_s]
    # print(df[df.date_of_measurement == "2022-04-26"].groupby(["weather_system"]).agg(Min=('temperature', 'min'), Max=('temperature', 'max')))
    print( df2a[df2a.for_date == "2022-04-28"])

# df.to_csv(r'../Previsoes/previsoes.csv', mode='a', header=False, index=False)
# df.to_csv(r'../Temperatura/temperatura.csv', mode='a', header=False, index=False)
