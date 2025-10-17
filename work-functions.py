# Work functions
# Author: Mia zhou
# October 10


# Average
def average(num_one: float, num_two: float, num_three: float) -> float:
    """Return the average"""
    # add all numbers together
    sum = num_one + num_two + num_three

    average = sum / 3

    return average


result = average(62, 61, 60)
print(result)

result = average(97, 95, 95)
print(result)
