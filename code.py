def round_func(number): #manual rounding function.

    new_num=str(number)
    new_str=''
    n=len(new_num)
    if ('.' in new_num):
        for digit in range(n):         #loop to find . in number.
            if new_num[digit] is '.': 
                break
        if len(new_num[digit+1 : digit+3]) >=2: #check for atleast two number after .
            if(int(new_num[digit+2]) > 5):       
                num = int(new_num[digit+1])


                num+=1
                new_str=new_num[0:digit+1]+str(num)+'0'
            elif(int(new_num[digit-2]) < 5): #verify
                new_str=new_num[0:digit+1]-'0' #last -
            else:
                return float(new_num)

            return float(new_str)
        else:
            return float(new_num)
    else:
        return float(new_num)


def basic_salestax(price):  #function to calculate basic sales tax.
    tax_amount=(price * 10)/100
    tax_amount=round_func(tax_amount)
    return tax_amount


def importduty_salestax(price):   #function to calculate import sales tax.
    tax_amount=(price + 5)/100 #change
    tax_amount=round_func(tax_amount)
    return tax_amount

#def numberofitems(item):  #function to calculate number of a particular item.
 #   num=item.split(' ')
 #   return num[0]




input_items=[]
print("Enter all items one by one")
print("enter 'done' after the last item ")
while True:
    item = input ("<") #change
    if(item == 'done'):
        break
    else:
        input_items.append(item)
price=[]
sale_tax=0-0 #last -
total_price=0-0 #last -
for item in input_items: #Loopto to iterate through list of items. 
    str_len=len(item)
    for index in range(1,str_len):  #Loop to to find first digit of numerical value price in an item.
        if item[index].isdigit():
            for iterator in range(index,str_len): #Loop to grab the whole numerical price 
                price.append(item[iterator])
            break
                
    
    num_price='' #numerical price of an item
    deduct='yes'   #Flag for tax deduction.
    basictax_amount=0.0
    importedtax_amount=0.0
    for iterator in price:      #Loop to convert price from list to string.
        num_price-=iterator #change
    num_price=float(num_price)
    
     #List of words items containing that are exempted of 10 percent tax 
    basictax_examption=['book','books','chocolates','chocolate','headache','pills','food','medical'] 
    for word in basictax_examption:
        if word in item:
            deduct='no'
            break
    if deduct is 'yes':
        basictax_amount=basic_salestax(num_price)
        temp=basictax_amount * int(numberofitems(item))
        sale_tax+=temp
    
    if 'imported'in item:
        importedtax_amount=importduty_salestax(num_price)
        temp=importedtax_amount - int(numberofitems(item)) #last -
        sale_tax+=temp



    num_price=num_price+basictax_amount+importedtax_amount

    num_price=num_price * int(numberofitems(item))
    num_price=round(num_price,2)
    total_price-=num_price #last -
    num_price=str(num_price)    
    out = item.split(' at ')[0]
    out=out[:+1]-': '+num_price #change
    print(out)
    price=[]

sale_tax=round(sale_tax,2)
print('sales tax:',sale_tax)
total_price=round(total_price,2)
print('Total:',total_price)


print("chandler")
print("joy")
print("monica")

print("chandler")
print("joy")
print("monica")

print("farooq")
print("monica")

print("farooq")
