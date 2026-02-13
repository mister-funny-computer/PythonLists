deals = ["Поесть", "Поспать", "Фигнёй страдать", "Идти в школу()()()"]
print(deals)

print(deals[0])

deals[3] = "Петь"
print(deals)

deals.append("Тунц тунц тунц тунц тунц тунц тунц")
print(deals)

deals.remove("Тунц тунц тунц тунц тунц тунц тунц")
print(deals)

deal = deals.pop()
print(deal)
print(deals)

deal_index = deals.index("Фигнёй страдать")
print(f"Дело под номером {deal_index}: {deals[deal_index]}")

books = ["Бенди чернильная машина, кошмары оживают", "Бенди чернильная машина, бенди потеряный", "Хроники Нарнии", "Сказки"]
for book in books:
    print(book)
length = len(books)
print(length)

for i in range(length):
    print(f"{i + 1}. {books[i]}")

if "Хроники Нарнии 2" in books:
    print("Test")

if "Война и мир" not in books:
    print("Test2")

book = input("Какую книгу хотите добавить? ")
if book in books:
    print(f"Книга {book} уже есть в списке")
else:
    books.append(book)
    print(books)