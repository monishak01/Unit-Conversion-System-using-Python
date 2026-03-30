def length_conversion():     
meters = 
float(input("Enter value in meters: "))     
km = 
meters / 1000     print("Kilometers:", km)  
def temperature_conversion():     
celsius = 
float(input("Enter temperature in Celsius: "))     
fahrenheit = (celsius * 9/5) + 32     print("Fahrenheit:", 
fahrenheit)  
def weight_conversion():     
kg = 
float(input("Enter weight in kg: "))     
grams = kg * 1000     print("Grams:", 
grams)  
print("----- Unit Conversion System -----") 
print("1. Length Conversion") print("2. 
Temperature Conversion") print("3. 
Weight Conversion")  
choice = int(input("Enter your choice: "))  
if choice == 1:  
length_conversion() elif 
choice == 2:  
temperature_conversion() elif 
choice == 3:     
weight_conversion()  
else:     
print("Invalid 
choice")  
