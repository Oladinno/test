ussd ='*909#'
t_pin = 1111
customerlist = []

def smenu4():
    #customerlist = []
    f_name = input('Enter First Name: ')
    l_name = input('Enter Last Name: ')
    dob = input('Enter Date of Birth: ')
    t_pin = input('Create 4 Digit PIN:')
    customerlist.append([f_name, l_name, dob, t_pin])
    print(customerlist)
    menu1()

def smenu1():
    airtime_self = int(input('Please Enter your PIN: '))
    if airtime_self == t_pin:
        c_amount = input('Please enter amount (50 - 10,000 \n :')
        print('transaction is being processed dial *909# to send money to someone')
    else:
        smenu1()

def smenu2():
    airtime_others = int(input('Please Input your PIN: '))
    if airtime_others == t_pin:
        dest_phone_num = input('Please enter destination phone number \n: ')
        c_amount = input('Please enter amount (50 - 10,000 \n :')
        print('transaction is being processed dial *909# to send money to someone')
        final = int(input('Would you like to save this beneficiary? \n 1. Yes \n 2. No  \n 00. Back  \n 0. Main \n :'))
        if final == 0:
            menu1()

def smenu3():
    check_bal = int(input('Please Enter your PIN: '))
    if check_bal == t_pin:
        balance = 5000
        t_fees = int(input('Transaction fee of N10 applies \n Do you wish to continue \n 1. Yes \n 2. No  \n 00. Back \n :'))
        if t_fees == 1:
            new_balance = balance - 10
            print(new_balance)
        elif t_fees == 2:
            smenu3()
        elif t_fees == 3:
            menu1()





def menu1():
    print(
        "Welcome to Central African Bank \n If you have an account with us proceed with your transaction \n if you don't please choose option 4 to Create one")
    print('1. Airtime Self')
    print('2. Airtime Others')
    print('3. Check Balance')
    print('4. Open Account')
    choice = int(input('Enter Choice Option '))
    if choice == 1:
        smenu1()
    elif choice == 2:
        smenu2()
    elif choice == 3:
        smenu3()
    elif choice == 4:
        smenu4()
    else:
        menu1()

def ussdc():
    while True:
        try:
            ussd = '*909#'
            code = input('Please Enter USSD CODE: ')
            if code == ussd:
                menu1()
        except:
            print('Wrong INPUT please Enter from the Options above')
            break
ussdc()