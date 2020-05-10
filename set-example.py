'''
set: set contains unique value
   : we cannot store duplicae
    : set will remove duplicate value automatically


'''

s= {'dove','iphone','dove','iphone'}
d= {11,22,1,11}

print(len(s))
print(s)
print(d)


for e in s:
    print(e)
    

#convert list to set (remove duplcate value)
d =[11,3,5,6,2,11,11,333]
print(d)

s =set(d) #convert to list, remove duplcate value
print(s)

    


