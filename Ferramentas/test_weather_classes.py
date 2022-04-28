import pytest
from weather_classes import Weather_system, Temperature, Temperature_range, Attribution, Current_temperature, Daily_forecast



def test_weather_systems_str():
    weather_s_a = Weather_system("a_b")
    assert str(weather_s_a) == "A B"

def test_weather_systems_repr():
    weather_s_a = Weather_system("A_b C.d")
    assert repr(weather_s_a) == "a_b_c_d"


def test_temperatures_str_positive():
    temp_a = Temperature(3, "K")
    assert str(temp_a) == "3°K"

def test_temperatures_str_negative():
    temp_a = Temperature(-3)
    assert str(temp_a) == "-3°C"

def test_temperatures_repr_positive():
    temp_a = Temperature(30, "F")
    assert repr(temp_a) == "30"

def test_temperatures_repr_negative():
    temp_a = Temperature(-30, "F")
    assert repr(temp_a) == "-30"

def test_temperatures_convert_to_c_f():
    # TODO implement test
    pass
    
def test_temperatures_convert_to_f_c():
    # TODO implement test
    pass

def test_temperatures_convert_to_f_k():
    # TODO implement test
    pass

def test_temperatures_convert_to_k_f():
    # TODO implement test
    pass

def test_temperatures_convert_to_k_c():
    # TODO implement test
    pass

def test_temperatures_convert_to_c_k():
    # TODO implement test
    pass

def test_temperature_ranges_str():
    temp_a = Temperature(-3, "F")
    temp_b = Temperature(3, "F")
    temp_range_a = Temperature_range(temp_a, temp_b)
    assert str(temp_range_a) == "Min: -3°F\nMax: 3°F"

def test_temperature_ranges_repr():
    temp_a = Temperature(-3)
    temp_b = Temperature(3)
    temp_range_a = Temperature_range(temp_b, temp_a)
    assert repr(temp_range_a) == "-3, 3"


def test_attributions_str():
    weather_s_a = Weather_system("baf_cap")
    attrib_a = Attribution(weather_s_a, "2022-05-01")
    assert str(attrib_a) == "By Baf Cap, at 2022-05-01"

def test_attributions_repr():
    weather_s_a = Weather_system("G HE")
    attrib_a = Attribution(weather_s_a, "2022-02-30")
    assert repr(attrib_a) == "g_he, 2022-02-30"


def test_current_temperatures_str():
    weather_s_a = Weather_system("a")
    temp_a = Temperature(3, "K")
    cur_temp_a = Current_temperature(weather_s_a, "2022-05-01", temp_a, "22")
    assert str(cur_temp_a) == "Temperature: 3°K as of 22h (By A, at 2022-05-01)"

def test_current_temperatures_repr():
    weather_s_a = Weather_system("A")
    temp_a = Temperature(-3, "F")
    cur_temp_a = Current_temperature(weather_s_a, "2022-01-25", temp_a, "18")
    assert repr(cur_temp_a) == "18, -3, a, 2022-01-25"


def test_daily_forecasts_str():
    weather_s_a = Weather_system("a")
    temp_a = Temperature(3)
    temp_b = Temperature(-3)
    temp_range_a = Temperature_range(temp_a, temp_b)
    daily_f_a = Daily_forecast(weather_s_a, "2022-04-25", temp_range_a, "2022-05-02")
    assert str(daily_f_a) == "On 2022-05-02, it's expected:\nMin: -3°C\nMax: 3°C\nBy A, at 2022-04-25"

def test_daily_forecasts_repr():
    weather_s_a = Weather_system("H_K.Law Ph")
    temp_a = Temperature(-3, "F")
    temp_b = Temperature(30, "F")
    temp_range_a = Temperature_range(temp_a, temp_b)
    daily_f_a = Daily_forecast(weather_s_a, "2022-04-26", temp_range_a, "2022-05-03")
    assert repr(daily_f_a) == "2022-05-03, -3, 30, h_k_law_ph, 2022-04-26"



