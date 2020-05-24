'''
User Defined Function: is also know custom function
                     - function is set of command or statement which can be reused
                     - function also support to modular programing, large code can written small unit/piece
                     - easy to maintain the source code 

Syntax to create function:
def fun_name():


There are following types of functions:
i. no argument no return
ii. no argument with return
iii. argument with no return
iv. argument with return
v. recussive function 
vi. lambda or anonyms function 


'''
#i. no argument no return
def welcome():
    print('This is test function, which can be useed')
    print('we are leraning function today...')
    print('this module contains following function i.welcome, ii. getdata iii. addNum iv. mul ')


#ii. no  argument with return
def getNum():
    a =input('enter data ')
    b =input('enter data ')
    return a,b
#iii. argument with no return
def addNum(n1,n2):
    c =n1+n2
    print 'sum of two numbers ',c 

#iv. argument with return
def mul(a,b):
    c =a*b 
    return c 
#v. recussive function  : function which call or invoke to itself, that function is known as recussive function 
def fact(n):
    if n==1:
        return n 
    else:
        return n * fact(n-1) # 6 * 5 * 4 * 3 * 2 *1 



#call or invoke to function 
welcome()
welcome()

x,y = getNum()
print x+y


a,b = getNum()
print a-b


addNum(4496,33)

addNum(449623,35553)

o = mul(11,33)
print o


out = mul(333,5) 
print(out)


f =fact(6)
print f

