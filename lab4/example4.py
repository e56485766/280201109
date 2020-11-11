a = int(input("a: "))
b = int(input("b: "))
 
answer = 1
 
for i in range(b):
    answer = a * answer
 
print(answer)