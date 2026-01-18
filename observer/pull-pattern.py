from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def registerObserver(self, observer):
        pass

    @abstractmethod
    def removeObserver(self, observer):
        pass
    @abstractmethod
    def notifyObservers(self):
        pass

class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass

class Observer(ABC):
    #No arguments! Just a "ping" that something changed.
    @abstractmethod
    def update():
        pass


class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0
    
    def registerObserver(self, observer):
        self.observers.append(observer)
    
    def removeObserver(self, observer):
        self.observers.remove(observer)

    # PUSH: We pass the state to the observers explicitly
    def notifyObservers(self):
        for obs in self.observers:
            obs.update()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notifyObservers()

    def getTemperature(self):
        return self.temperature

    def getHumidity(self):
        return self.humidity

    def getPressure(self):
        return self.pressure


class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, weatherData:WeatherData):

        self.weatherData = weatherData
        self.weatherData.registerObserver(self)
        
        self.temperature = 0.0
        self.humidity = 0.0
        self.pressure = 0.0

    def update(self):
        temperature = self.weatherData.getTemperature()
        humidity = self.weatherData.getHumidity()
        pressure = self.weatherData.getPressure()
        
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature}F degrees and {self.humidity}% humidity")
