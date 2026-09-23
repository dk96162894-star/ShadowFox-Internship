# Task 1 - Numbers

# Question 1
def format_number(number, character):
    return "{0}{1}".format(number, character)


result = format_number(145, "o")
print("Question 1:", result)

# Representation used: positional representation
# {0} -> first argument (145)
# {1} -> second argument ("o")


# Question 2
radius = 84
pi = 3.14

area = pi * radius ** 2
print("Question 2 - Pond Area:", area)

# Bonus
water_per_square_meter = 1.4
total_water = area * water_per_square_meter

print("Bonus - Total Water:", int(total_water))


# Question 3
distance = 490
time_minutes = 7

time_seconds = time_minutes * 60
speed = distance / time_seconds

print("Question 3 - Speed:", int(speed), "m/s")