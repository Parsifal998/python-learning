def deposit(balance, user_sum):
    result = balance + int(user_sum)
    return result

def withdraw(balance, user_sum):
     if int(user_sum) <= balance:
         result = balance - int(user_sum)
         return result
     elif int(user_sum) > balance:
         print("Недостатньо коштів!")
         return balance
         

def show_balance(balance):
    print(balance)

balance = 0

while True:
    
    print("Оберіть дію: ")
    print("1 - поповнити баланс")
    print("2 - витратити кошти")
    print("3 - показати баланс")
    print("4 - вихід")
    user_input = input()

    if int(user_input) == 1:
        print("Введіть бажану суму: ")
        user_sum = input()
        balance = deposit(balance, user_sum)

    elif int(user_input) == 2:
        print("Введіть бажану суму: ")
        user_sum = input()
        balance = withdraw(balance, user_sum)

    elif int(user_input) == 3: 
        show_balance(balance)

    elif int(user_input) == 4:
        break