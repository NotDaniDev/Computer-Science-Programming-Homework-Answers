Lower_Num=int(input("Enter the first number for range: "))
Upper_Num=int(input("Enter the second number for range: "))

print("Display the even numbers between two numbers are: ")
for i in range(Lower_Num,Upper_Num+1):
    if(i%2==0):
        print(i)

print("Display the odd numbers between two numbers are: ")
for i in range(Lower_Num,Upper_Num+1):
    if(i%2==1):
        print(i)