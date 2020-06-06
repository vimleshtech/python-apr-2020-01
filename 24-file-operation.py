
file =open(r'output.txt','r')

data =file.readlines()

#get row count
print('row count ',len(data))


#get word count
wc =0
for row in data:
    word = row.split(' ')
    wc += len(word)

print('word count ',wc)

#get char count
cc =0
for row in data:

    cc += len(row)

print('char count ',cc)


