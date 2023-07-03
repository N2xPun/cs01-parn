wScore = int(input("Please enter your work score: "))
mScore = int(input("Please enter your midterm score: "))
fScore = int(input("Please enter your final score: "))

score = wScore + mScore + fScore
grade = "invalid"

if (score >= 80 and score <= 100):
    grade = "A"
elif (score <= 79 and score >= 75):
    grade = "B+"
elif (score <= 74 and score >= 70):
    grade = "B"
elif (score <= 69 and score >= 65):
    grade = "C+"
elif (score <= 64 and score >= 60):
    grade = "C"
elif (score <= 59 and score >= 55):
    grade = "D+"
elif (score <= 54 and score >= 50):
    grade = "D"
elif (score <= 49 and score >= 0):
    grade = "F"
else:
    print("Your score is invalid.")

print("Your grade is " + str(grade) + ".")