n = int(input("write a number "))
from itertools import permutations

numbers = sorted(list(set(int(''.join(p)) for p in permutations(str(n)))))
max_int = max(numbers)

if max_int == n:   # <- fixed here
    print(-1)
else:
    print(numbers[numbers.index(n) + 1])

