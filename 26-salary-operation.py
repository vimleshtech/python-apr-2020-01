
##wap to read data from file and get the total sal
f = open('users.txt') #default file mode is read (r)

#skip the first row/ header
f.readline() #read first line


#now read all data except first line 
data = f.readlines()

sal = 0

for row in data:
    col = row.split(',')
    sal = sal+  int(col[3]) 
    
    #print(row)


print('total sal ',sal)



