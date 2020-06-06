
file =open(r'C:\Users\Vimlesh.Kumar\Documents\Development\aws_codecommit\CodeCommit-Build-Pipeline.txt','r')

print(file)
#print(file.read()) #read all content
#print(file.readline()) #read one line

#print(file.readlines())#read all lines and convert to list

data = file.readlines()

for row in data:
    print(row)


file.close()








