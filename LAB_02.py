print ("Michael Mordec, 6/11/22, Lab 2, CSC 242:")
# ---------------------------------------------------
custID = 0
custName = ""
custAddress = ""
custKHU = 0
custAmountPastDue = 0
# ---------------------------------------------------
def getCustomerData() :

    global custID, custName, custAddress, custKHU, custAmountPastDue
    
    custName =                input("please enter the Customer Name   : ")   
    custID =                 (input("please enter the Customer Number : "))
    custAddress =            (input("please enter Customer address    : "))
    custKHU =             int(input("please enter Kilowatt Hours used : "))
    custAmountPastDue = float(input("please enter Amount Past Due     : "))

    print (custID)

# ---------------------------------------------------
def calculateElecticBill() :
    totalBill = 0
    if(custKHU < 125):
        totalBill = .10*custKHU
    elif(custKHU >= 125 and custKHU <320):
        totalBill =  12.5+.09*(custKHU-125)
    elif(custKHU >= 320 and custKHU <500):
        totalBill =  30.6+.08*(custKHU-320)
    elif(custKHU >= 500):
        totalBill =  42.6+.06 *(custKHU-500)
    else:
        return 0
    if(custAmountPastDue>0):
        totalBill += custAmountPastDue*1.025
    return totalBill
# ---------------------------------------------------
print ()

# call the functions
getCustomerData()
totalBill = calculateElecticBill()


# ---------------------------------------------------
# display the Electricity Bill Summary
print ("\nElectricity Bill\n")
print ("\n****************\n")
print ("Customer ID Number    ", custID)
print ("Customer Name         ", custName)
print ("Customer Address      ", custAddress)
print ("Kilowatt- Hours used  ", custKHU)
print ("Amount Past Due       ", custAmountPastDue)
print ("Total Bill            ", totalBill)

