import math                 #import statement
print()
heading="Finance calculator"        #Title for the project
new_heading = heading.center(100," ") #center function to display the Title in centre
print(new_heading)
print("\ninvestment  - to calculate the amount of interest you'll earn on your investment")     #menu
print("bond        - to calculate the amount you'll have to pay on a home loan\n")              #menu
user_input = input("\nEnter either 'investment' or 'bond' from the menu above to proceed :")        #user input to choose investment or bond

if (user_input == "investment") or (user_input == "Investment") or (user_input == "INVESTMENT"):    #we check the user input using or operator using if statement
    interest = input("\n Enter simple interest or compound interest: ")                              #user input to choose interest 
    if (interest == "simple interest") or (interest == "Simple") or (interest == "simple") or(interest == "SIMPLE INTEREST"):  #we check the user input using or operator using nested if
        print("\n Details for simple interest \n")
        invest_amount = int(input("\t Enter the deposit amount:"))                         #user input to get principal amount
        s_interest = int(input("\t Enter the interest rate in percentage :"))                #user input to get rate of interest
        invest_interest = s_interest/100
        invest_period = int(input("\t Enter the investment period in years:"))              #user input to get number of years
        simple_interest= invest_amount*(1+invest_interest*invest_period)
        print("\n Simple interest for your deposit : ", round(simple_interest))
        print()
    elif (interest == "compound interest") or (interest == "Compound") or (interest == "compound") or (interest== "COMPOUND INTEREST"):#we check user input
        print("\n Details for compound interest \n")
        invest_amount = int(input("\tEnter the deposit amount:"))                          #user input to get deposit amount
        c_interest = int(input("\tEnter the interest rate in percentage :"))                 #user input to get rate of interest
        invest_interest = c_interest/100
        invest_period = int(input("\tEnter the investment period in years:"))               #user input to get number of year
        compound_interest= invest_amount* math.pow((1+invest_interest),invest_period)
        print("\n Compound Interest for your deposit :", round(compound_interest))
        print()
elif (user_input == "BOND") or (user_input == "bond") or (user_input == "Bond"): #we check user input 
    print("\nDetails for bond repayment\n")
    value_house = int(input("\tEnter the present value of house : "))                   #user input to get present value of house
    bond_interest_rate = int(input("\tEnter the interest rate : "))                     #user input to get interest rate
    bond_interest = (bond_interest_rate/100)
    interest= (bond_interest/12)
    number_months= int(input("\tEnter the number of months they plan to take to repay the bond : ")) #user input to get number of months to repay the bond
    repayment_amount= (interest*value_house)/(1-(1+interest)**(-number_months))
    print("\n The repay amount by user for every month : ", round(repayment_amount))
    print()

else: #we check user_input 
    alert="ALERT!!!!! Please enter only either 'investment' or 'bond' to proceed!!!"
    new_alert = alert.center(100," ")                                       #center function to display the alert message in centre
    print()
    print(new_alert)
    print()