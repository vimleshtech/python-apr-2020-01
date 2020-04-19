#nested loop
'''
123
123
123
'''

for i in range(1,4):
    for  j in range(1,4):
        print(j,end='') #print and don't change line 
    print() #new line 
    

'''
1
12
123
1234
'''
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end='')
    print()

'''
123
12
1
'''
for i in range(4,0,-1):
    for j in range(1,i):
        print(j,end='')
    print()


    




    
        
        
