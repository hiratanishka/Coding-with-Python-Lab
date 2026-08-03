"""
Program : Weather−Bot 3000
Purpose : Gives simple lifestyle advice based on temperature and rain
Author : Tanishka Hira
Date : 03-08-2026
"""

#Task 1
print(42 == 42) #True
print('AI' == 'ai') #False
print(10 > 5 and 2 < 1) #True and False = False


#Task 2
curr_temp = input("enter current temperature in Celsius: ") #str
if curr_temp.isdigit() is True:
    curr_temp_in_int = int(curr_temp) #int
    if curr_temp_in_int > 30:
        print("It’s hot! AI suggests turning on the AC.")
    else:   
        if curr_temp_in_int < 15:
            print("Chilly! AI suggests a jacket.")
        else:
            print("Temperature is optimal. Enjoy your day.")

    rain = input("Is it raining ? ") #whether it's raining or not
    if "Yes" or "yes please" or "YES" in rain.check.lower():
        print("Carry an umbrella.")
    else:
        print("Dont carry an umbrella")
else:
    print("please write in digits")

