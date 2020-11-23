email = input("Email Adress: ").lower().split("@")
wanted_email = "ceng113@example.com"

if email.count("@") == 1:

  email = email[0].replace(".", "") + "@" + email[1]

  if email == wanted_email:
    print("Yes, it is ceng113@example.com")
  else:
    print("No, it is not ceng113@example.com")

else:
  print("No, it is not ceng113@example.com")