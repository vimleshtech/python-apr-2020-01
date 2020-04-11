#WAP to take three input from user and show the greater number

a = int(input('enter number '))
b = int(input('enter number '))
c = int(input('enter number '))

if a>b:
    if a>c:
        print('a is greater')
    else:
        print('c is greater')
        
else:
    if b>c:
        print('b is greater')
    else:
        print('c is greater')
        
#or
if a>b and a>c:
    print('a is greater')
elif b>a and b>c:
    print('b is greater')
else:
    print('c is greater')



    
