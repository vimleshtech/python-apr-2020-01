
#create function
#have to pass two arguments 
def add(a,b): #argument with no return 

    c =a+b
    print(c)

#argument with default value, all arguments are optional 
def addNum(a=0,b=0,c=0,d=0):

    m = a+b+c+d
    print(m)


#- argument with dynamic count of inputs
def mul(*arg): #receive n number of argument
    print(arg) #print all data
    print(type(arg)) #print type of var: tuple 
    n  = 1
    for x in arg:
        n*=x

    print(n)
    

#call to function
add(11,344)

addNum(11,33)
addNum(11,33,44)
addNum(11,33,4,55)


addNum(1)#error
addNum()
addNum(1,2)


mul(11,33,5,6,7,4)
mul(11,33,5,6,7,4,555,2,2,2,4,6,3)


