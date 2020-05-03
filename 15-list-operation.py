sales =[111,44,6,3,66,777]

#sales all data
print(sales)

#print len
print(len(sales))

#sum
print(sum(sales))

#min
print(min(sales))

#max
print(max(sales))

#sort
sales.sort() #in asc
print(sales)

#reverse
sales.reverse()
print(sales)


#copy
b= sales.copy() #copy data from sales to b
print(b)


#extend
b.extend(sales)
print(b)


#add new value : append
sales.append(10000)
sales.append(66)
sales.append(100)
print(sales)


#remove from last:
sales.pop()
print(sales)

#insert value at given location
sales.insert(2,5000)#add 5000 at 2nd position
print(sales)

#find and reove if exist
sales.remove(5000)
print(sales)

#get the count
c=sales.count(777)
print(c)


#slicer
print(sales[0]) #first value
print(sales[-1])  #last value
print(sales[0:4]) # from 0 till 3
print(sales[:4]) # from 0 till 3

print(sales[2:6]) #

#print in reverse
print(sales[::-1]) #:: print right to left, -1 decrementer
print(sales[::-2]) #2 step decrementer

























