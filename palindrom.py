user_word = input()
lower_word = user_word.lower()
palindrom = lower_word [::-1]

if lower_word == palindrom:
    print("Це паліндром")

else:
    print("Це не паліндром")
