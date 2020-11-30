books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]

book_dict = {}

for i in books:
  unique_char = set(i)
  average = (len(i) + len(unique_char)) / 2
  book_dict[i] = (len(i), len(unique_char), average)

print(book_dict)

for i in book_dict:
  print(i, "->", book_dict[i])