# Question 1
def format_number(number, representation):
    return format(number, representation)

result = format_number(145, 'o')
print(result)


# Question 2
radius = 84
pi = 3.14

area = pi * radius * radius
print("Area of pond:", area)

water_per_square_meter = 1.4
total_water = area * water_per_square_meter

print("Total water:", total_water)


# Question 3
distance = 490
time_minutes = 7

time_seconds = time_minutes * 60

speed = distance / time_seconds

print("Speed:", speed, "m/s")