shopping_list = []
def add_item(shopping_list, towar):
    shopping_list.append(towar)
    pass

def show_list(shopping_list):
    print(shopping_list)
    pass

def remove_item(shopping_list, towar):
    shopping_list.remove(towar)
    pass

while True: 
    print("Оберіть дію: ")
    print("1 - додати товар")
    print("2 - показати список")
    print("3 - видалити товар")
    print("4 - вихід")
    user_input = input()

    if int(user_input) == 1:
        print("Введіть назву товару: ")
        towar = input()
        add_item(shopping_list, towar) 
        
    elif int(user_input) == 2:
        show_list(shopping_list)
        
    elif int(user_input) == 3:
        print("Введіть назву товару: ")
        towar = input()
        remove_item(shopping_list, towar)

    elif int(user_input) == 4:
        break