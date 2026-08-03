def converter(temp, from_unit, to_unit):
    if from_unit == "C":
        if to_unit =="F":
            return (temp*9/5)+32
        if  to_unit == "K":
            return temp + 273.15
    if from_unit == "F":
        if to_unit == "C":
            return (temp-32)*5/9
        if to_unit == "K":
            return (temp-32)*5/9 + 273.15
        
temp=input("Enter the temperature: ")
from_unit=input("Enter the unit of the temperature (C/F/K): ")
to_unit=input("Enter the unit to convert to (C/F/K): ")
print(f"The converted temperature is: {converter(float(temp), from_unit, to_unit)}")