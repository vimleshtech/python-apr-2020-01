
w1= {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
w2 = {2:'twenty',3:'thirty',4:'fourtey',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninty'}


n = int(raw_input('enter numebr '))
if n<20:
    print w1[n]
elif n<100:
    n1=n//10  # example: 34  = 3
    n2=n%10   #          34  = 4
    
    # 90 80 
    if n2>0:
        print w2[n1],w1[n2]
    else:
        print w2[n1]





    






