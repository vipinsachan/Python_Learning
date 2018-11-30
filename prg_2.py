#program to convert temperatures to and from celcius, fahrenheit

unit=input("To convert Celsius to Fahrenheit => press 1 and To convert Celsius to Fahrenheit => press 2: ")
temp=int(input("What is the temperature: "))
flag=1

while flag == 1:
    if int(unit) == 1:
        c=(5/9)*(temp-32)
        print("Fahrenheit to celsius: ", c)
        flag = 0
    elif int(unit) == 2:
        f=((9/5)*temp) + 32
        print("Celsius to Fahrenheit: ", f)
        flag = 0
    else:
        print("Please press either 1 or 2...")
        print("To convert Celsius to Fahrenheit => press 1 and To convert Celsius to Fahrenheit => press 2: ")
        flag = 1