import random

# Generation of random temperature and humidity values
temperature = random.uniform(10.0, 40.0)  # temperature in degrees Celsius
humidity = random.uniform(10.0, 60.0)  # rhumidity in percentage

# Check for high temperature and high humidity conditions
if temperature > 30.0 and humidity > 30.0:
    print("Current Temperature:", round(temperature,2), "°C")
    print("Current Humidity:", round(humidity,2), "%")
    print("High temperature and high humidity detected!")
    print("----------ALARM ON----------")

# If only the temperature exceeds its threshold, we print a warning message
elif temperature > 30.0:
    print("Current Temperature:", round(temperature,2), "°C")
    print("Current Humidity:", round(humidity,2), "%")
    print("Warning: High temperature detected!")

# If only the humidity exceeds its threshold, we print a warning message    
elif humidity > 30.0:
    print("Current Temperature:", round(temperature,2), "°C")
    print("Current Humidity:", round(humidity,2), "%")
    print("Warning: High humidity detected!")

# If neither condition is met, we turn the alarm off
else:
    print("Current Temperature:", round(temperature,2), "°C")
    print("Current Humidity:", round(humidity,2), "%")
    print("Everything looks fine!")
    print("----------ALARM OFF----------")





    







    

  
