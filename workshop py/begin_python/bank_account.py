#ishika=25,000
#Functions|arithmetic operations|listwelcome
#1. language
#2. Domestic|international
#3. pin number
#4. deposit|withdraw|check_balance|pin_change|fast_withdrawal
#5. Thankyou

balance=50000
pin='2345'
name='Ishika'

print('Welcome to Canara Bank!',name)

def lang():
    print('Choose Language:')
    print('1. English')
    print('2. Hindi')
    language=int(input('Enter 1 or 2:'))
    if language==1:
       print('English')
    elif language==2:
       print('Hindi')

def loc():
    print('Choose Location:')
    print('1. Domestic')
    print('2. International')
    location=int(input('Enter 1 or 2:'))  
    if location==1:
        print('Domestic')
    elif location==2:
        print('International')

def pin_no():
    for _ in range(3):
       new_pin=int(input('Enter PIN:'))
       if new_pin==int(pin):
           print('Correct pin , take access')
           return True
       else:
           print('Incorrect pin, Try Again')
    return False

def choose(balance):
    print('Choose:')
    print('deposit')
    print('withdraw')
    print('check')
    print('exit')
    work=input('Enter what you want to choose:').lower()
    if work=='deposit':
       amt=int(input('Enter the amount to be deposited :'))
       balance =balance+ amt
       print(f'{amt} is deposited , balance now : {balance}')


    elif work=='withdraw':
       amt=int(input('Enter the to withdraw :'))
       if amt<=balance:
          balance =balance-amt
          print(f'{amt} is withdrawn , balance now :{balance}')
       else:
          print('Insufficient access') 

    elif work =='check':
        print(f'Your balance :{balance}')

    elif work =='exit':
        print('Bye!!')
        return None

    else: 
        print('Invalid Input , Please Try Again')  
        return balance

def call():
    lang()
    loc()

    if pin_no():  
        balance_updated = balance
        while True:
            balance_updated = choose(balance_updated)
            if balance_updated is None:  
                break
        print('Thank you!')
    else:
        print('Your attempts are finished, Failed')

call()
