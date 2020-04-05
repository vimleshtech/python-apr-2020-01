#WAP to input two number and get sum of that value

n1 =int(input('enter data :')) #read data and convert to int
n2 =int(input('enter data :')) #read data and convert to int

#get the some the two values 
n =n1+n2

print('sum of two values ',n)

#with format
print('sum of n1 and n2 is n')
print('sum of {} and {} is {}'.format(n1,n2,n)) #use the placeholder

#manual index
print('sum of {1} and {0} is {2}'.format(n1,n2,n))

#error
#print('sum of {1} and {0} is {}'.format(n1,n2,n))

#or
print(f'sum of {n1} and {n2} is {n}')





