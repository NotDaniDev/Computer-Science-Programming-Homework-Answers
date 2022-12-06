a = int(input("Input a year: "))
if a % 4 == 0:
    print(a, "is a leap year.")
elif a % 4 == 1 or a % 4 == 2 or a % 4 == 3:
    print(a, "is not a leap year")
else:
    print("Invalid Input.")