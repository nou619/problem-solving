# Next Bigger Number Finder
# This script takes a number input from the user and finds the next bigger number
# that can be formed by rearranging its digits.
# If the number is already the largest permutation, it returns -1.

# Ask the user to input a number and convert it to an integer
n = int(input("write a number "))

# Import permutations function from itertools module
from itertools import permutations

# Generate all possible unique permutations of the digits of n
# 1. str(n) converts the number to a string so digits can be iterated
# 2. permutations(str(n)) generates all possible orderings of digits
# 3. ''.join(p) joins the tuple of characters into a string
# 4. int(''.join(p)) converts the string back to an integer
# 5. set(...) removes duplicate permutations
# 6. list(...) converts the set back to a list
# 7. sorted(...) sorts the numbers in ascending order
numbers = sorted(list(set(int(''.join(p)) for p in permutations(str(n)))))

# Find the largest number in the list of permutations
max_int = max(numbers)

# Check if the input number is already the largest possible permutation
if max_int == n:
    # If yes, print -1 because no bigger permutation exists
    print(-1)
else:
    # Otherwise, find the index of n in the sorted list
    # Print the next number in the list, which is the next bigger permutation
    print(numbers[numbers.index(n) + 1])
