#WAP to take sales amt from user and show total included tax


amt = int(input('enter amt '))
tax = 0

if amt>1000:
    tax = amt*.18 #18% tax  #  amt*18/100 
elif amt>500:
    tax = amt*.12
elif amt>200:
    tax = amt*.05
else:
    tax = amt*.02
    
    

total = amt+tax
print('total amt is ',total)
