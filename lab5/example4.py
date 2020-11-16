correct_password = "abc123"

while True:
  password = input("Enter password: ")
  if password == "help":
    print(correct_password[0])
  elif password != correct_password:
    print("Wrong")
  else:
    print("Welcome")
    break
