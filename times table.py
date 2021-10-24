print("\n" * 2)
n = int(input("Enter a number (1 to 30): "))

if n <= 0:
    print(f"{n} that number is too low so using 1")
    n = 1

if n > 30:
    print(f"{n} is too high so using 30")
    n = 30

print("\n" * 2)
print("*\t" * (n + 2))
print("")
for i in range(1, n + 1):
    print("*", end="\t")
    for x in range(1, n + 1):
        print(i * x, end="\t")
    print("* \n")
print("*\t" * (n + 2))
