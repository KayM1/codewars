# given is an array n, with an undertermined number of floats and a goal total
# the fuction must find all possible combinations of numbers in n that would add up to total
import random

def sum_finder(n, goal, max_length=3):
    from itertools import combinations
    # Function to find all combinations of a given length that sum to the goal
    def find_combinations_of_length(n, goal, length):
        return [list(comb) for comb in combinations(n, length) if sum(comb) == goal]

    result = []
    for length in range(2, max_length + 1):
        combs = find_combinations_of_length(n, goal, length)
        if combs:
            result.extend(combs)
            # print(f"Combinations of length {length}: {combs}")

    return result

# Example usage:
# n = [0.5, 0.9, 6.3, 10.2, 11.1, 11.5, 12.2, 12.3, 13.3, 13.7, 14.3, 15.9, 17.8]
# goal = 37.7

# combinations = sum_finder(n, goal)
# for combi in combinations:
#     print(f"{combi} together add up to {goal}. \n")

# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# goal = 10
# combinations = sum_finder(n, goal)
# for combi in combinations:
#     print(f"{combi} together add up to {goal}. \n")

result_f = 0
while result_f < 5:
    # Generate a list of 100 random floats between 0 and 20
    n = [round(random.uniform(0, 20), 1) for _ in range(50)]
    # Set a viable goal (e.g., the sum of 4 randomly selected numbers from the list)
    goal = sum(random.sample(n, 10))//1

    # print("List of numbers:", n)
    # print("Goal:", goal)

    combinations = sum_finder(n, goal, 2)
    for combi in combinations:
        if combi == combinations[-1]:
            print(f"{combi} together add up to {goal}. \n")
            result_f += 1