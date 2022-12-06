num = int(input('Enter the three digit number to be checked for Armstrong: '))
t = num
cube_sum = 0

while t!= 0:
    k = t % 10
    cube_sum += k**3
    t = t//10
if cube_sum == num:
    print(num, ' is an Armstrong Number')
else:
    print(num, 'is not a Armstrong Number')