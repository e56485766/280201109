# Write a Python code to ask user to enter
# two values: one for GPA and the other for
# Number of Lectures. According to the below
# table, decide whether user will be
# graduated or not. If not, give an
# appropriate message as given table.

gpa = float(input("Your GPA: "))
num_lectures = int(input("Number of your lectures: "))

if gpa < 2.0 and num_lectures < 47:
    print("Not enough number of lectures and GPA!")
elif gpa >= 2.0 and num_lectures < 47:
    print("Not enough number of lectures!")
elif gpa < 2.0 and num_lectures >= 47:
    print("Not enough GPA!")
else:
    print("GRADUATED!!!")