# Write a Python program that asks user for
# age and calculates ticket price accordingly:
# − Normal bus ticket price is 3 TL.
# − Bus ticket price for people younger than
# 6 and older than 60 years old is free.
# − People whose age are between 6 and 18
# take 50% discount.

ticket_price = 3
age = int(input("How old are you?  "))

if age < 6 or age > 60:
    ticket_price = 0
elif age <= 18:
    ticket_price *= .5
else:
    ticket_price = 3

print(ticket_price)