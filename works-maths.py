# Maths stuff with python
# November 12, 2025
# Author: Mia Zhou

#
#
#

#


def main():
    # Question 1
    current_age = int(input())

    # Difference


if __name__ == "__main__":
    main()

# Question 1
# get current age from user
current_age = int(input("How old are you now?"))
# Calculate age in 2049
age_in_2049 = current_age + 24
# Display the result
print(f"In 2049 you will be(age_in_2049)years old")

# Question 2
# Get scores from 5 judges
score1 = float(input("Judge 1: "))
score2 = float(input("Judge 2: "))
score3 = float(input("Judge 3: "))
score4 = float(input("Judge 4: "))
score5 = float(input("Judge 5: "))

# Calculate the avergae
average_score = (score1 + score2 + score3 + score4 + score5) / 5

# Display the result with 1 decimal place
print(f"Your Olympic score is{avergae_score:.1f}")

# Question 3
# Initialize the total cost
total = 0

# Ask about burger
burger = input("Wpuld you like a burger for $5? (Yes/No) ").lower()
if burger == "yes":
    total += 5

# Ask about fries
fries = input("Woul you like some fries for $3? (Yes/No) ").lower()
if fries == "yes":
    total += 3

# Add 14% tax
total_with_tax = total * 1.14

# Display the total formatted to 2 decimal places
print(f"Your total is ${total_with_tax:.2f}")
