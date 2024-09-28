# I want to check if a number can be represented by 3 exponents of 2
# so if a number n = 2**i + 2**j + 2**k

# first of all, any duplicate combinations of i, j and k are useless to us

from functools import lru_cache

@lru_cache(maxsize=None)
def generate_combinations():
    unique_combinations = set()

    # Generate all combinations of three integers from 0 to 100 (inclusive)
    for i in range(0, 101):
        for j in range(i, 101):
            for k in range(j, 101):
                combo = (i, j, k)
                unique_combinations.add(combo)

    return unique_combinations

@lru_cache(maxsize=None)
def calculate_values():
    unique_combinations = generate_combinations()
    combo_values = {combo: 2**combo[0] + 2**combo[1] + 2**combo[2] for combo in unique_combinations}
    return combo_values

def exp3(n):
    combo_values = calculate_values()

    # Create a reverse dictionary to find combinations by value
    value_to_combo = {value: combo for combo, value in combo_values.items()}

    # Check if the given number n is in the calculated values
    if n in value_to_combo:
        combo = value_to_combo[n]
        return f"The number {n} can be represented as 2^{combo[0]} + 2^{combo[1]} + 2^{combo[2]}. The combination is {combo}."

    # If n is not found, find the closest lower and higher values
    sorted_combos = sorted(combo_values.items(), key=lambda item: item[1])
    
    lower = None
    higher = None

    for combo, value in sorted_combos:
        if value < n:
            lower = (combo, value)
        elif value > n:
            higher = (combo, value)
            break

    lower_str = f"2^{lower[0][0]} + 2^{lower[0][1]} + 2^{lower[0][2]} = {lower[1]}" if lower else "None"
    higher_str = f"2^{higher[0][0]} + 2^{higher[0][1]} + 2^{higher[0][2]} = {higher[1]}" if higher else "None"

    return f"The number {n} cannot be represented as a sum of three powers of 2. Closest lower is {lower_str}, and closest higher is {higher_str}."

# Test the function
print(exp3(7))  # Example: 7 == 2^0 + 2^1 + 2^2
print(exp3(8))  # Example: 8 == 2^3
print(exp3(15)) # Example: 15 == 2^0 + 2^1 + 2^2 + 2^3 (which is not a valid case for 3 exponents)





