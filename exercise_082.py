class Thermostat():
	def __init__(self, initial_temperature = 0):
		self.__temperature = initial_temperature

	def __str__(self):
		return f"the thermostat is a temperature of: {self.__temperature}°C"

	@property
	def temperature(self):
		return self.__temperature
	
	@temperature.setter
	def temperature(self, value):
			if not (-273.15 <= value <= 1000):
				print("Error: Temperature outside of range.")
			else:
				self.__temperature = value

	def celsius_to_fahrenheit(self):
		return (self.__temperature * 9/5) + 32
