x = input("please input the value you want to check: ")
xRev = x[::-1]
if x.lower() == xRev.lower():
    print(f"{x} is a palindrome")
else:
    print(f"{x} is not a palindrome")