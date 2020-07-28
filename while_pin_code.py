##########  DATALAYER   #########

CLIENT_SECRET_PIN = 1234
CLIENT_FULL_NAME  = "John Doe"
CLIENT_BANK_ID    = "123abc567xyz"

############ LOGIC & USER INTERFACE ########
print("~" * 40)
user_pin = int(input("PIN1: "))
user_pin_1 = 0
user_pin_2 = 0
if user_pin == CLIENT_SECRET_PIN:
    print("welcome")
while user_pin != CLIENT_SECRET_PIN: 
    user_pin_1 = int(input("PIN2: "))
    if user_pin_1 != CLIENT_SECRET_PIN:
        print("Mai aveti o sansa")
    else:
        print("welcome")

    while user_pin_1 != CLIENT_SECRET_PIN:
        user_pin_2 = int(input("PIN3: "))
        if user_pin_2 != CLIENT_SECRET_PIN:
            print("blocat")
        else:
            print("welcome")
        break
    break




