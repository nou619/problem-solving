# Van Eck Sequence Generator in Python
# ------------------------------------
# This program generates the Van Eck sequence, a sequence of numbers
# where each term depends on the last occurrence of the previous term.
#
# Rules:
# 1. Start with a0 = 0
# 2. For each subsequent term:
#    - If the previous term has never appeared before, the next term is 0
#    - Otherwise, the next term is the distance to the last occurrence
#
# Implementation:
# - Uses a tuple list `lst` to track both the index and value of each term
# - Builds a string `ch` to display the sequence
# - Uses `second_elements[::-1].index(prev)` to find the last occurrence of the previous term
#
# Example:
# Input: n = 5
# Output: 0 0 1 0 2
# Explanation:
# Term 0: 0 (initial)
# Term 1: 0 (0 appeared before at index 0 → next = 0)
# Term 2: 1 (0 appeared before → distance = 2 → next = 1)
# Term 3: 0 (1 first occurrence → 0)
# Term 4: 2 (0 last appeared at index 1 → distance = 2)
#
# Notes:
# - Works for any n
# - Keeps the history of all terms to correctly calculate distances
# - Uses string concatenation to build the output sequence
