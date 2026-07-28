
def count_vowels(word):
    vowels = "аеёиоуыэюя"
    count = 0

    for letter in word:
        if letter in vowels:
            count = count + 1
    return count
            

print(count_vowels("Ярослав"))
