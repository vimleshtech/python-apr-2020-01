fname =input('enter the file name :')


f =open(fname,'a') #w- overwrite the data, a - append the data in existing data


for i in range(5):
    data = input('enter data :')
    f.write(data+'\n')


f.close() #save the file
print('file is closed')


