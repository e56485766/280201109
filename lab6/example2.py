grades = [[50,90,60],[15,60,75],[99,95,91]]
student_count = len(grades)
average_grades = []

for i in range(student_count ):
  average = grades[i][0] * .3 + grades[i][1] * .3 + grades[i][2] * .4
  average_grades.append(average)

print(average_grades)