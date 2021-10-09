#                   Compulsory Task

########################################################################################

# Import math

import math

# Declare variable for initial output the user sees
# A welcome message and a brief introduction of our finacial calculator

Message = """\n\t\tWELCOME TO AUTHENTIC BANKING SOLUTIONS

Choose either 'investment' or 'bond' from the menue below to proceed :

Investment\t- to calculate the amount of intrest you'll earn on intrest.
Bond\t\t- to calculate the amount you'll have to pay on a home loan.

"""

# Print initial Message

print(Message)

# Request user input to determine which calculator to used 'Investment' or 'Bond'

User_selection = input("Please enter Selection Here : ")

# If user selection equals to investment perform calculation

if(User_selection.lower() == "investment"):                                                         # Use lower function to insure input is all in lower case

    User_Deposit = float(input("\nHow much will you be depositing : R"))                            # Declare variables for calculations
    Interest_Rate = float(input("At what INTEREST RATE' as a percentage '%' : "))
    Expected_time = float(input("How many years do you plan on investing for : "))
    
    interest = input("\nFor Simple interest enter\t-  'simple'\nFor Compound interest enter\t- 'compound'\n\n----> : ")     # Declare variable to determine weather simple intrest or compound intrest
    
    if(interest.lower() == "simple"):
        Simple_interest = round(User_Deposit * ( 1 + ( Interest_Rate / 100 ) * Expected_time ),2)                           # Formula for simple interest
        
        print(f"\nInitial Deposit\t\t: R{User_Deposit}\nInterest Rate\t\t: {Interest_Rate}%\n\nThe total amount once the interest has been applied over {Expected_time} years is : R{Simple_interest}\nThank You!")         # Print Output

    elif(interest.lower() == "compound"):
        Compound_interest = round(User_Deposit * math.pow(( 1 + ( Interest_Rate / 100 )), Expected_time ),2)                # Formula for compound intrest
                                                                                        
        print(f"\nInitial Deposit\t\t: R{User_Deposit}\nInterest Rate\t\t: {Interest_Rate}%\n\nThe total amount once the interest has been applied over {Expected_time} years is : R{Compound_interest}\nThank You!")       # Print Output

    else:                                                                                                                   # Else if user eneters invalied input between 'Simple' & 'Compound' display output
        print("\nThat funny!!!!\n\nIt seems like that input was invalied, please restart the program !")                    # Print Output


elif(User_selection.lower() == "bond"):                                                                                     # For 'Bond' calculations
    
    Present_value = float(input("\nWhat is the present value of the house : R"))                                            # Request user input and declare variables
    Interest_Rate = float(input("At what 'ANNUAL INTEREST RATE' : "))
    Expected_time = int(input("How many months do you plan to take to repay the bond (eg: 120 ) : "))

    Repayment_total = round(((Interest_Rate/100)/12 *Present_value)/(1 - pow((1+(Interest_Rate/100)/12),-1*Expected_time)),2)       # Formula for bond repayment
    
    print(f"\nPresent Value\t\t: R{Present_value}\nAnnual Intrest\t\t: {Interest_Rate}'%\n\nYour monthly payments will result to  : R{Repayment_total}\nThank You!!!")      #Print Output

else:
    print("\n***Seems like you have entered an invalid entry, please restart the program.***")                              # Ask user to restart program if an invalid input is entered between 'Bond' & 'Investment'

# END
