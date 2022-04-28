class Weather_system():
    """
    A company/entity that attributes temperature values through measurements or forecasts
    """
    def __init__(self, name: str):
        self._name = name
    
    def __str__(self) -> str:
        return self._name.replace("_", " ").title()
    
    def __repr__(self) -> str:
        return self._name.replace(" ", "_").replace(".", "_").lower()
    
    def __lt__(self, other: object) -> bool:
        return str.__lt__(self.name, other.name)

    @property           
    def name(self): 
        return self._name
    
    @name.setter   
    def name(self, new_name: str):   
        self._name = new_name  
    
    @name.deleter
    def name(self):  
        del self._name


class Temperature():
    """
    A value on a scale of C (celsius), F (Fahrenheit) or K (Kelvin)
    """
    _T_UNITS = ["C", "F", "K"]

    def __init__(self, value: float, unit: str = "C"):
        # TODO check if unit is within possible units, raise error if not
        # TODO check if temperature values are within the helm of possibility
        self._value = float(value)
        self._unit = unit.upper()

    def __str__(self) -> str:
        return f"{str(self._value)}°{self._unit}"
    
    def __repr__(self) -> str:
        return f"{str(self._value)}"
    
    def __eq__(self, __o: object) -> bool:
        return float.__eq__(self._value, __o.value)

    def __lt__(self, __o: object) -> bool:
        return float.__lt__(self._value, __o.value)
    
    def __le__(self, __o: object) -> bool:
        return float.__le__(self._value, __o.value)
    
    def __gt__(self, __o: object) -> bool:
        return float.__gt__(self._value, __o.value)
    
    @property           
    def value(self): 
        return self._value

    @value.setter   
    def value(self, new_value: float):   
        self._value = new_value 
    
    @value.deleter
    def value(self):  
        del self._value

    @property           
    def unit(self): 
        return self._unit

    @unit.setter   
    def unit(self, new_unit: float):   
        self._unit = new_unit
    
    @value.deleter
    def unit(self):  
        del self._unit

    def convert_to(self, to_unit: str = "F"):
        """
        Converts a temperature value from it's current unit to an equivalent value of desired unit
        """
        if to_unit[0].upper in self.__T_UNITS and to_unit[0].upper != self.unit:
            if self.unit == "C":
                if to_unit.upper == "F":
                    self.value = self.value * 9 / 5 + 32
                if to_unit.upper == "K": 
                    self.value += 273
            if self.unit == "F":
                self.value = (self.value - 32) * 5 / 9
                if to_unit.upper == "K": 
                    self.value += 273
            if self.unit == "K":
                self.value -= 273
                if self.unit == "F":
                    self.value = self.value * 9 / 5 + 32
            self._unit = to_unit.upper
            

class Temperature_range():
    """
    Two related temperatures - maximum and minimum temperatures
    """
    def __init__(self, min: Temperature, max: Temperature):
        if min.value <= max.value:
            self._min = min
            self._max = max
        else:
            self._min = max
            self._max = min

    def __str__(self) -> str:
        return f"Min: {self._min.__str__()}  Max: {self._max.__str__()}"
    
    def __repr__(self) -> str:
        return f"{self._min.__repr__()}, {self._max.__repr__()}"
    
    @property           
    def min(self): 
        return self._min

    @property           
    def max(self): 
        return self._max

    
class Attribution():
    """
    Measure or prediction made by a weather system at given date
    """
    def __init__(self, weather_system: Weather_system, date_of_attribution: str):
        self._weather_system = weather_system
        self._date_of_attribution = date_of_attribution
    
    def __str__(self) -> str:
        return f"By {self._weather_system.__str__()}, at {self._date_of_attribution}"
    
    def __repr__(self) -> str:
        return f"{self._weather_system.__repr__()}, {self._date_of_attribution}"

    @property           
    def weather_system(self) -> Weather_system: 
        return self._weather_system

    @property           
    def date_of(self) -> str: 
        return self._date_of_attribution


class Current_temperature(Attribution):
    """
    A measurement of temperature made by a weather system at a given time of a given day
    """
    def __init__(self, weather_system: Weather_system, date_of_attribution: str, temperature: Temperature, time_of: str):
        Attribution.__init__(self, weather_system, date_of_attribution)
        self._temperature = temperature
        self._time_of = time_of
    
    def __str__(self) -> str:
        return f"Temperature: {self._temperature.__str__()} as of {self._time_of}h ({Attribution.__str__(self)})"
    
    def __repr__(self) -> str:
        return f"{self._time_of}, {self._temperature.__repr__()}, {Attribution.__repr__(self)}"

    def __dict__(self):
        return {
            'weather_system': self._weather_system,
            'date_of_measurement': self._date_of_attribution,
            'temperature': self._temperature,
            'time_of_measurement:' : self._time_of
        }



class Daily_forecast(Attribution):
    """
    A range of temperatures (min and max temp) expected to occur at_date as forecast by a weather_system at date_of_attribution
    """
    def __init__(self, weather_system: Weather_system, date_of_attribution: str, temperature_range: Temperature_range, at_date: str):
        Attribution.__init__(self, weather_system, date_of_attribution)
        self._temperature_range = temperature_range
        self._at_date = at_date

    def __str__(self) -> str:
        return f"On {self._at_date}, it's expected:\n{self._temperature_range.__str__()}\n{Attribution.__str__(self)}"
    
    def __repr__(self) -> str:
        return f"{self._at_date}, {self._temperature_range.__repr__()}, {Attribution.__repr__(self)}"

    def __dict__(self):
        return { 
            'date_of_attribuition': self._date_of_attribution, 
            'weather_system': self._weather_system, 
            'temperature_range': self._temperature_range, 
            'for_date' : self._at_date
        }
        