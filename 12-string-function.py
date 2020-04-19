#string input
s = input('enter string data :')


print(s)
print(len(s))
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())

print(s.replace('a','xy'))

l = list(s) #convert char by char
print(l)

l.sort()
print(l)


word = s.split(' ') #convert word by word
print(word)

print(s.count('a'))


if s.isdigit():
    print('number value ')
else:
    print('string ')


if s.isupper():
    print('in upper case')
else:
    print('in lower')






if s.islower():
    print('in lower case')
else:
    print('in upper ')

    





if s.isdigit():
    print('number value ')
else:
    print('string ')




    











