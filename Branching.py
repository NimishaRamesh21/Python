a = int(input("Enter a score: "))

if a >= 90 and a <= 100:
    print("Student's grade is A and passed successfully")
elif a >= 80 and a <= 89:
    print("Student's grade is B and passed successfully")
elif a >= 70 and a <= 79:
    print("Student's grade is C and passed successfully")
elif a >= 60 and a <= 69:
    print("Student's grade is D and passed successfully")
elif  a < 60:
    print("Student's grade is F ")
else:
    print("Invalid score entered!")
