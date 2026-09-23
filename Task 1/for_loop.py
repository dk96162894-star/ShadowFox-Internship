# Task 1 - For Loop

import random


# Question 1 - Roll a six-sided die 20 times

rolls = []

for i in range(20):
    roll = random.randint(1, 6)
    rolls.append(roll)

print("Dice rolls:", rolls)

# Count how many times 6 was rolled
six_count = rolls.count(6)

# Count how many times 1 was rolled
one_count = rolls.count(1)

# Count two 6s in a row
two_six_count = 0

for i in range(len(rolls) - 1):
    if rolls[i] == 6 and rolls[i + 1] == 6:
        two_six_count += 1

print("Number of times 6 was rolled:", six_count)
print("Number of times 1 was rolled:", one_count)
print("Number of times two 6s occurred in a row:", two_six_count)


# Question 2 - Jumping Jacks

total_jumping_jacks = 0

for i in range(10):
    total_jumping_jacks += 10

    print("\nYou completed", total_jumping_jacks, "jumping jacks.")

    if total_jumping_jacks == 100:
        print("Congratulations! You completed the workout!")
        break

    tired = input("Are you tired? (yes/no): ").lower()

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()

        if skip == "yes" or skip == "y":
            print("You completed a total of", total_jumping_jacks, "jumping jacks.")
            break

    elif tired == "no" or tired == "n":
        remaining = 100 - total_jumping_jacks
        print(remaining, "jumping jacks remaining.")