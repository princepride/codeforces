import math
def flagstones_needed(n, m, a):
    # Calculate the number of flagstones needed along the width and height
    width_stones = math.ceil(n / a)
    height_stones = math.ceil(m / a)
    
    # Calculate the total number of flagstones needed
    total_stones = width_stones * height_stones
    
    return total_stones

# Read the input values
n, m, a = map(int, input().split())

# Call the function and print the result
print(flagstones_needed(n, m, a))