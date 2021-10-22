x = int(input("Enter number: "))
a = x
f = a
while 1 < x:

    print(x, f)
    x = x - 1
    f = f * x

print(f" The factorial of {a} is {f}")
