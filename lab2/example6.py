# Write a program that solves the following
# problem:
# There are two cars that start at the same
# time and drive towards each other. Velocity
# of the cars are fixed at 80 km/h and 70
# km/h. At the beginning, the distance
# between the cars is 490 km. After how many
# minutes will the distance between them be
# 150 km?

car1 = 80
car2 = 70
distance = 490
wanted_distance = 150

total_velocity = car1 + car2
distance_difference = distance - wanted_distance
minutes = (distance_difference * 60)/wanted_distance

print(minutes)