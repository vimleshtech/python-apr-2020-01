
n = int(input('enter data :'))
d = int(input('enter data :'))


try:

    if d<0:
        msg = ZeroDivisionError ('divisor cannot be less than 0')
        raise msg #go to error block (except block)
    
    o =n/d

    print('div ',o)

    #ZeroDivisionError
    #ValueError
    #NameError
except ZeroDivisionError as er:
    print(er)
except:
    pass

finally:
    print('end of code ')
    


#add
s = n+d
print('sum ',s)



