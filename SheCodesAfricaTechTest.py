# Fibonacci number sequence of first fifteen numbers

n1 = 0
n2 = 1

f =[n1,n2]

for i in range(0,14):
    n3 = n1+n2
    f.append(n3)
    n1=n2
    n2=n3

print(f)

