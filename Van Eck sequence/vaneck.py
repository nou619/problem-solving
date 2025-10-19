n=int(input('enter n'))
lst=[]
a=0
ch=''
for i in range(n):
    if lst == []:
        lst.append((i,0))
        ch = ch + " " + str(a)
    else:
        second_elements = [t[1] for t in lst]
        prev = lst[-1][1]  # previous term
        if prev not in second_elements[:-1]:  # exclude last
            a = 0
        else:
            j = len(lst) - 2 - second_elements[:-1][::-1].index(prev)
            a = i - 1 - j
        lst.append((i,a))
        ch = ch + " " + str(a)

print(ch.strip())


        

