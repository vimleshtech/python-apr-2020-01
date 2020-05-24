

unit = int(input('enter unit '))

amt =0
if unit<100:
    amt = unit*.40
elif unit<300:
    amt = 40+(unit-100)*.50
else:
    amt = 140+(unit-300)*.60 #first 100 = 40 + 200 = 100 
total = amt+50
print('total amt ',amt)

