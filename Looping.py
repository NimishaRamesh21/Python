sum =0
mul=1
for i in range(1, 6, 1):
    if i % 2 == 0:
        sum += i
    else:
        mul *= i

    print("Sum is:", sum)
    print("Mul is:", mul)

for i in range(1,6):
    for j in range(1,6):
        print("*", end=" ")
    print() 

# Tasks
for i in range(1,6):
    for j in range(1,6):
        print(i, end=" ")
    print() 

print("-----")
for i in range(1,6):
    for j in range(1,6):
        print(j, end=" ")
    print()
print("-----")
for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(i, end=" ")
    print() 

print("-----")
for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(j, end=" ")
    print()

