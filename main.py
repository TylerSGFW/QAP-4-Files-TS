#Program for the One Stop Insurance Company to enter and calculate policy information for customers.
#Author: Tyler Stuckless     Date: November 29, 2022


#Opens OSICDef.dat to read the constants.
f = open("OSICDef.dat", "r")

NEXT_POLICY_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
AUTO_DISCOUNT = float(f.readline())
EXTRA_LIA = float(f.readline())
GLASS_COVER = float(f.readline())
LOANER_COVER = float(f.readline())
HST_RATE = float(f.readline())
PROCESSING_FEE = float(f.readline())

f.close()

#Accepts user input in a loop.
while True:
    FirstName = input("Enter the first name: ").title()
    LastName = input("Enter the last name: ").title()
    CustAddress = input("Enter the address: ").title()
    CustCity = input("Enter the city: ").title()
    Province = input("Enter the province: ").title()
    PostalCode = input("Enter the postal code:")
    PhoneNum = input("Enter the phone number:")
    CarAmount = int(input("Enter the number of cars: "))
    LiabilityChoice = input("Enter your choice of extra liability up to $1,000,000 (Y for Yes, N for No): ").upper()
    GlassChoice = input("Enter your choice of optional glass coverage (Y for Yes, N for No): ").upper()
    LoanerChoice = input("Enter your choice of an optional loaner car (Y for Yes, N for No): ").upper()
    PayType = input("Enter your choice of payment (F for Full, M for Monthly): ").upper()

    #Performs calculations based on inputs.
    Discount = BASIC_PREM * AUTO_DISCOUNT
    ExtraPrice = BASIC_PREM - Discount
    InsurPrem = BASIC_PREM + ((CarAmount - 1) * ExtraPrice)
    if LiabilityChoice == "Y":
        LiaExtra = EXTRA_LIA
    else:
        LiaExtra = 0
    if GlassChoice == "Y":
        GlassExtra = GLASS_COVER
    else:
        GlassExtra = 0
    if LoanerChoice == "Y":
        LoanerExtra = LOANER_COVER
    else:
        LoanerExtra = 0
    TotalExtra = LiaExtra + GlassExtra + LoanerExtra
    HST = InsurPrem * HST_RATE
    TotalCost = InsurPrem + HST
    MonthPay = (TotalCost + PROCESSING_FEE) / 8

    #Prints receipt to the screen.
    print("    One Stop Insurance Company")
    print("    Customer Policy Information")
    print("-------------------------------------------------------")
    print(f" First name: {FirstName:<8}        Last name: {LastName:<8}")
    print(f" Address: {CustAddress:<15}    City: {CustCity:<10}")
    print(f" Province: {Province:<10}        Postal code: {PostalCode:<8}")
    print(f" Phone number: {PhoneNum:<10}    Amount of cars: {CarAmount:>3}")
    if LiabilityChoice == "Y":
        print(" Extra liability: Yes")
    else:
        print(" Extra liability: No")
    if GlassChoice == "Y":
        print(" Glass coverage: Yes")
    else:
        print(" Glass coverage: No")
    if LoanerChoice == "Y":
        print(" Loaner car: Yes")
    else:
        print(" Loaner car: No")
    print(f" Insurance premium: {InsurPrem:<6}  Additional car price: {ExtraPrice:<6}")
    print(f" Discount: {Discount:<6}            Total extra costs: {TotalExtra:<6}")
    print(f" HST: {HST:<6}               Total cost: {TotalCost:<6}")
    if PayType == "M":
        print(f" Monthly payment: {MonthPay:<6}")

    #Saves inputs and policy number to a file for future reference.
    f = open("Policies.dat", "a")

    f.write("{}, ".format(str(NEXT_POLICY_NUM)))
    f.write("{} ,".format(FirstName))
    f.write("{} ,".format(LastName))
    f.write("{} ,".format(CustAddress))
    f.write("{} ,".format(CustCity))
    f.write("{} ,".format(Province))
    f.write("{} ,".format(PostalCode))
    f.write("{} ,".format(PhoneNum))
    f.write("{} ,".format(str(CarAmount)))
    f.write("{} ,".format(LiabilityChoice))
    f.write("{} ,".format(GlassChoice))
    f.write("{} ,".format(LoanerChoice))
    f.write("{} ,".format(PayType))
    f.write("{}\n".format(str(InsurPrem)))

    f.close()

    print()
    print("Policy information processed and saved.")
    #Increments the policy number by one.
    NEXT_POLICY_NUM += 1

    #Saves the constants and the new policy number.
    f = open("OSICDef.dat", "w")

    f.write("{}\n".format(str(NEXT_POLICY_NUM)))
    f.write("{}\n".format(str(BASIC_PREM)))
    f.write("{}\n".format(str(AUTO_DISCOUNT)))
    f.write("{}\n".format(str(EXTRA_LIA)))
    f.write("{}\n".format(str(GLASS_COVER)))
    f.write("{}\n".format(str(LOANER_COVER)))
    f.write("{}\n".format(str(HST_RATE)))
    f.write("{}\n".format(str(PROCESSING_FEE)))

    f.close()

