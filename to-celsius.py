#Converting Fahrenheit to Celsius code.

fahrenheit = float(input("What temperature (in Fahrenheit) would you like converted to Celsius? ")) 

celsius = (fahrenheit -32) * 5 / 9 

#Used the round function to make the return value rounded to 2 decimal places.

print(fahrenheit, "F is", round(celsius, 2), "C")

