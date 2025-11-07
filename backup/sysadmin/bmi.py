#!/usr/bin/env prython3.9
# BMI = (weight in kg / height in meters squared)
# Imperial version: BMI * 703

def gather_info():
    height = float(input("Whats is your height? (inches or meters)"))
    weight = float(input("Whats is your weight? (pounds or kilograms)"))
    system = input("Are your mesurements in metric or imperial units? ").lower().strip()
    return (height, weight, system)


def calculate_bmi(weight, height, system="metric" ):
    """
    Return the Body Mass Index (BMI) for the
    given weight, heght, and measurement system.
    """
    if system == "metric":
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gather_info()
    if system.startswith("i"):
        bmi = calculate_bmi(weight, system=system, height=height)
        print(f"your BMI is {bmi}")
        break
    elif system.startswith("m"):
        bmi = calculate_bmi(weight, height)
        print(f"your BMI is {bmi}")
        break
    else:
        print("Error: unknow measurment system. Please use imperial or metric." )