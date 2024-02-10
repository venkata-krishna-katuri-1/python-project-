print("\n\n\t\t\t\t\t WELCOME TO FRIENDS MART  ")
print("\t\t\t\t\t ------------------------- ")
cusname=str(input("ENTER CUSTOMER NAME ::==:: "))
cusid=str(input("ENTER 'ID' OR 'PHONE NUMBER' ::==:: "))
print("\n")
product=[0]
mrp=[0]
mp=[0]
qt=[0]
price=[0]
discount=0
totalbill=0
choice=0
count=0
total_cost=0
for i in range(1,150):
    print("\n")
    pname=str(input(" ENTER THE PRODUCT {0} NAME ::== ".format(i)))
    pname=pname.upper()
    mrpp=float(input(" ENTER THE  {n} {m} PRICE::== ".format(n=pname,m="'M R P'")))
    mpp=float(input(" ENTER THE  {n} {m} PRICE::== ".format(n=pname,m="'M A R T'")))
    quantp=float(input(" ENTER THE  {n} {m} ::== ".format(n=pname,m="'QUANTITY'")))
    product.append(pname)
    mrp.append(mrpp)
    mp.append(mpp)
    qt.append(quantp)
    price_for_list=mp[i]*qt[i]
    price.append(price_for_list)
    disc=(mrpp-mpp)*quantp
    discount+=disc
    totalbill+=price[i]
    count+=1
    total_cost+=price[i]
    print("\n\n TOTAL COST ::== {0:12.2f} RS\n".format(total_cost))
    choice=int(input(" "))
    if choice==2:
        continue
    else:
        break
for y in range(1,10):
    print(" \n\t\t MODE OF PAYMENT :: \n\n \t\t 1. CASH \n\t\t 2. UPI PAYMENTS \n\t\t 3. SORRY WE HAD ABOVE OPTIONS ONLY ")
    modcash=int(input("\n\t\t ENTER THE NUMBER ::==:: "))
    if modcash==1:
        print(" \n\n\t\t PAY THE AMOUNT OF {0:12.2f} RS\n ".format(total_cost))
        cash=int(input("\t\tCUSTOMER TOTAL PAID AMOUNT ::==:: "))
        balance=cash-total_cost
        BAL1=float(balance)
        print("\n\t\t BALANCE GIVEN = {0:12.2f} RS".format(BAL1))
        BILLNO=int(input("\n\t\t PRESS 1 TO GET BILL == "))
        if BILLNO==1:
            print("\n")
            break
        else:
            continue
    elif modcash==2:
        print(" \n\n\t\t PAY THE AMOUNT OF {0:12.2f} RS\n ".format(total_cost))
        print("      \t\tUPI PAYMENTS ID == 9132918314@YBHLS ")
        BILLNO=int(input("\n\t\t PRESS 1 TO GET BILL == "))
        if BILLNO==1:
            print("\n")
            break
        else:
            continue
    else:
        continue
print("\n\n\t\t\t$$$$ TOTAL BILL $$$$\n______________________________________________________________________________________________________________________________")
print("{0:^8} |  {1:<30}  | {2:^10}   | {3:^6}      | {4:^10}    | {5:^10}".format(' S.NO ',' PRODUCT ',' M R P ',' M P ','QUANTITY',' PRICE '))
print("_____________________________________________________________________________________________________________________________________")

for i in range(1,count+1):
    print("{0:^8} |  {1:<30}  | {2:^10.2f}   | {3:^6.2f}      | {4:^10.3f}    | {5:^10.2f} ".format(i,product[i],mrp[i],mp[i],qt[i],price[i]))
print("\n\n")
print("HI {0} , PLEASE PAY THE AMOUNT OF   ==  {1:15.2f} RS".format(cusname.upper(),totalbill))
print("                    YOU HAD SAVED   ==  {0:>15.2f} RS".format(discount))
print("                    TOTAL PRODUCTS  ==  {0:>15} PRODUCTS".format(i))
print("\n\n\t\t\t THANK YOU AND VISIT AGAIN \n\n\n")
# Open the file in append mode
with open('customer_data.txt', 'a') as file:
    file.write("\n\n---------------------------------------------\n")
    file.write("Customer Name: {}\n".format(cusname))
    file.write("Customer ID/Phone: {}\n".format(cusid))
    
    for i in range(1, count + 1):
        file.write("\nProduct {}: {}\n".format(i, product[i]))
        file.write("MRP: {}Rs\n".format(mrp[i]))
        file.write("MP: {}Rs\n".format(mp[i]))
        file.write("Quantity: {}\n".format(qt[i]))
        file.write("Price: {}Rs\n".format(price[i]))

    file.write("\nTotal Bill: {}Rs\n".format(totalbill))
    file.write("Total Discount: {}Rs\n".format(discount))
    file.write("Total Products: {}\n".format(count))

