#for loop
for x in range(1,11):
    print(x)
    

for x in range(10,0,-1):
    print(x)


#wap to get sum of all even and odd numbers between two given input
n1 =int( input('enter data :'))
n2 =int( input('enter data :'))

se = 0
so = 0

for x in range(n1,n2):
    if x%2 ==0:
        se =se+x
    else:
        so =so+x

print('sum of all even ',se)
print('sum of all odd ',so)






    
    
        
