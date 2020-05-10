#wap to convert digit to word
# 123  = one hundered twenty three

'''
dict: is key value pair
'''
d ={'a':'alpha',1:'hundered',10:'ten',
    'd':'delta','b':5000,'m':'monday'}

print(type(d))
print(d) #print all data

print(d.keys())#print all keys
print(d.values()) #pritn all values

#read value by key
print(d['b'])

#modify the value
d['b'] = 9044
print(d['b'])

#add new key
d['t']='tata'
print(d)


for k,v in d.items(): #k will receive the key, and v will receive the value 
    print(k,v)



#search key by value    
for k,v in d.items(): #k will receive the key, and v will receive the value
    if v=='tata':
        print(k)







    





