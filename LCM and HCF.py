x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
if x>y:
    bigger = x
else:
    bigger = y

while(True):
    if((bigger%x==0) and (bigger%y==0)):
        lcm = bigger
        break
    bigger += 1
print(f'Lowest Common Multiple of the 2 numbers you entered is {lcm}')

if x>y:
    smaller = y
else:
    smaller = x
for i in range(1,smaller+1):
    if ((x%i==0) and (y%i==0)):
        hcf = i
print(f'Highest Common Factor of the 2 numbers you entered is {hcf}')
