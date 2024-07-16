import time

password = 1234
balance = 50000
deposit = 0

def Check_Balance():
    print(f"Your current balance is : {balance}\nThank You!")

def withdraw():
    withdrawal_amount = int(input("Enter the amount that you want to withdraw: "))
    if withdrawal_amount > balance:
        print("You do not have sufficient balance. Please Try Again!")
    else:
        print("Transaction Successful!")

def Cash_deposit():
    global balance
    deposit = int(input("Enter the amount you want to Deposit: "))
    balance += deposit
    print(f"Now Your balance is: {balance}")

def PIN_Change():
    global pin
    ans = input("Do you really want to change your PIN?\nYES or NO? ")
    if ans.lower() == "yes":
        pin = int(input("Enter your new PIN: "))
        print("PIN changed successfully!")
    else:
        print("No changes were made to your PIN.")

def main():
    requirement = int(input("Choose the option:\n1. Check balance\n2. Withdraw cash\n3. Deposit cash\n4. PIN change\n"))
    
    if requirement == 1:
        Check_Balance()
    elif requirement == 2:
        withdraw()
    elif requirement == 3:
        Cash_deposit()
    elif requirement == 4:
        PIN_Change()
    else:
        print("Invalid option selected. Please try again.")
        
main()