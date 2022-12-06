nth_term = int(input('Enter the number of terms you want in the series: '))
n1,n2=0,1
count = 0
print('Fibonacci Sequence: ')
while count<nth_term:
    print(n1)
    nth = n1+n2
    n1 = n2
    n2 = nth
    count+=1