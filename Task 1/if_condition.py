# Task 1 - If Condition


# Question 1 - BMI Category

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

print("BMI:", bmi)

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")


# Question 2 - City and Country

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("\nEnter a city name: ")

if city in Australia:
    print(city, "is in Australia")
elif city in UAE:
    print(city, "is in UAE")
elif city in India:
    print(city, "is in India")
else:
    print("City not found")


# Question 3 - Check whether two cities belong to the same country

city1 = input("\nEnter the first city: ")
city2 = input("Enter the second city: ")

country1 = None
country2 = None

if city1 in Australia:
    country1 = "Australia"
elif city1 in UAE:
    country1 = "UAE"
elif city1 in India:
    country1 = "India"

if city2 in Australia:
    country2 = "Australia"
elif city2 in UAE:
    country2 = "UAE"
elif city2 in India:
    country2 = "India"

if country1 == country2 and country1 is not None:
    print("Both cities are in", country1)
else:
    print("They don't belong to the same country")