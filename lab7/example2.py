books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]

book_dict = {}

for book in books:
  unique_char = set(i)
  book_dict[i] = (len(i), len(unique_char))

print(book_dict)