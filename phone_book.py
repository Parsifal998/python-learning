def remove_contact(phone_book, name):
    del phone_book[name]

phone_book = {
    "Іван": "0928172635",
    "Мария": "0384756453"
}

print(phone_book["Іван"])
phone_book["Ярослав"] = "0998273746"

print(phone_book)