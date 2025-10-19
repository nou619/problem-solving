n = int(input('Enter n: '))  # Number of terms in the sequence
lst = []                      # List to store tuples (index, value)
a = 0                          # Current term
ch = ''                        # String to build the output sequence

for i in range(n):
    if lst == []:  # First element
        lst.append((i, 0))
        ch += str(a) + " "
    else:
        second_elements = [t[1] for t in lst]  # All previous values
        prev = lst[-1][1]                       # Previous term
        if prev not in second_elements[:-1]:    # If prev never appeared before
            a = 0
        else:
            # Find last occurrence of prev before the previous term
            j = len(lst) - 2 - second_elements[:-1][::-1].index(prev)
            a = i - 1 - j
        lst.append((i, a))
        ch += str(a) + " "

print(ch.strip())  # Print the sequence as space-separated numbers