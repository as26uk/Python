import time

a = int(input("Enter number of stars: "))
i = 0
while i < a:
    i += 1
    print("*" * i, end="")
    print(i)
    time.sleep(0.5)

