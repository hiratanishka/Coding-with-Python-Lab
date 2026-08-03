'''
Program : Temporal Profile Analyzer
Purpose : Computes an AI Era Readiness Score from user metadate.
Author  : Tanishka Hira
Date    :
'''

import datetime
name = input("Enter your full name: ")
new_name = name.strip()
identifier_byte_count = len(new_name)
print(identifier_byte_count)
title_case_name = new_name.title()
print(title_case_name)

age=input ("your current age: ")
if age.isdigit() is True: 
    age_in_num=int(age)
    today= datetime.date.today()
    year_now=today.year
    years=2045-year_now
    age_in_2045=age_in_num+years
    score = ((identifier_byte_count*10) + age_in_2045)/2
    print("\n========== USER REPORT ==========")
    print("Formatted Name :", title_case_name)
    print("Identifier Byte Count :", identifier_byte_count)
    print("Current Age :", age_in_num)
    print("Age in 2045 :", age_in_2045)
    print("AI Readiness Score :" f"{score:.2f}")
    print("You will be", age_in_2045, "in 2045.")
    print(f"{score:.2f}")
    a = age_in_num//10 
    print(title_case_name*a)
else:
    print("Please enter numbers.")
