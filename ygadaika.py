secret_number = 52.2

print("Відгадайте загадане число: ")
while True:
    
    number = input()
    if float(number) > secret_number:
        print("Загадане число менше!")

    elif float(number) < secret_number:
        print("Загадане число більше!")

    else:
        print("Вітаю, ви вгадали!")
        break


