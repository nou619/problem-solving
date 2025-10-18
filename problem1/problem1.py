n=int(input("write a number "))
from itertools import permutations
numbers=sorted(list(set(int(''.join(p)) for p in permutations(str(n)))))
max=max(numbers)
if(max==n):
    print(-1)
else:
    print(numbers.index(n)+1)
