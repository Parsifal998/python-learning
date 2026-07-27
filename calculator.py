secret_number = 1111111111111111111111111111111111111

print("Відгадайте загадане число: ")
while True:
    
    number = input()
    if int(number) > secret_number:
        print("Загадане число менше!")

    elif int(number) < secret_number:
        print("Загадане число більше!")

    else:
        print("Вітаю, ви вгадали!")
        break


