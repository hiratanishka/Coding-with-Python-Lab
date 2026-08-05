"""
Program: Climatic Risk Intelligence Module
Purpose: Classify environmental risk levels using temperature, humidity, wind speed, and battery level.
Author: Tanishka Hira
Date: 05-08-2026
"""

if temp := input("Temperature (in C): ").strip():
    try:
        temperature = float(temp)
        humid = input("Humidity (in %): ").strip()
        humidity = float(humid)
        assert humidity >= 0, "Telemetry Error: Negative Humidity"

        wind_str = input("Wind speed (in km/h): ").strip()
        wind_speed = float(wind_str)

        hsi = temperature+(0.5*humidity)
        print("\nHeat Stress Index (HSI):", hsi)
        if temperature <= 0:
            tier = "FREEZE ALERT"
        elif hsi > 45 or (temperature > 38 and humidity > 70):
            tier = "CRITICAL"
        elif 30 <= hsi <= 45 and wind_speed < 5:
            tier = "CAUTIONARY"
            #if classified cautionary
            battery = input("Battery level(in %): ").strip()
            battery_level = float(battery)
            if battery_level < 20:
                tier = "CRITICAL"
            elif battery_level > 80:
                tier = "OPERATIONAL"
        else:
            tier = "OPERATIONAL"
        print("\nSafety Level:", tier)

        risk_label = "Safe" if hsi < 30 else "Unsafe"
        print("Risk Label:", risk_label)

    except ValueError:
        print("Safety Level: Unknown")

    except AssertionError as error:
        print(error)

else:
    print("Safety Level: Unknown")
