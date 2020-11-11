# Write a Python program that reads a month and
# day from the user. Your program should display the
# season associated with the date that was entered.

month = int(input("Month: "))
day = int(input("Day: "))

if month < 3 and day < 20:
    season = "Winter"
elif month < 6 and day < 21:
    season = "Spring"
elif month < 9 and day < 22:
    season = "Summer"
elif month < 12 and day < 21:
    season = "Fall"

print(season)