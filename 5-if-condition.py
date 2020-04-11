#WAP to take sales amt from user and show total included tax
#tax should be applicabe if amt is greater than 1000

amt = int(input('enter amt '))
tax = 0

if amt>1000:
    tax = amt*.18 #18% tax  #  amt*18/100 


total = amt+tax
print('total amt is ',total)
