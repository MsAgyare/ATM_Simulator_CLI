# Welome user
# Ask user to insert card
print("Welcome to MEST AFRICA ATM \nPlease insert your atm card\n")

#Ask user to insert card details to detect type of card
user_card_name= input("Please enter the name of your card here:\n")
user_card_number= input("Enter the last 4 digits of your card number here:\n")

# ask user to enter pin
user_card_pin = int(input("Enter atm pin here:\n"))

# store user's current balance
current_balance = 10000.00

#authenticate user's pin
def pin_authentication(pin):
    user_card_pin = int(input("Enter atm pin here:\n"))
    while True:
        try:
            if user_card_pin == pin:
                print("Login successful")
            else:
                print("Pin authentication failed")
                break
        except ValueError:
            print("Invalid pin. Try again")
    return user_card_pin

# call pin_authentication function
pin_authentication()

# define function for withdrawal
def withdrawal():
    global current_balance
    amount = float(input("Enter the amount to withdraw here:\n"))
    if amount <= 0:
        print("Invalid entry. Enter correct amount")
    if amount <= current_balance:
        current_balance -= amount
        print("withdrawal successful, please take your cash and card.")
    else:
        print("Insufficient balance")

# define function for choices
def choices():
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdram money")
    print("4. Transaction history")
    print("5. Exit")

    options = input("Choose an option here")
    if options == "1":
        print(f"Your existing balance is GHS {current_balance}")
    elif options == "2":
        print("Ready to deposit")
    elif options == "3":
        withdrawal()
    elif options == "4":
        print("Transaction History")
    elif options == "5":
        print("Exit")
    else:
        print("Choose from the otions")
        
choices()
