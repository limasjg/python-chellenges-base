unit = input("What is your temperature unit (C/F)? ")
temp = float(input("How many degrees is it now? "))

if unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature em Celcius is {temp}C")
elif unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature em Fahreinheint is {temp}F")
else:
    print(f"{unit} Not is valid")
