wScore = int(input("Please enter your work score: "))
mScore = int(input("Please enter your midterm score: "))
fScore = int(input("Please enter your final score: "))
grades = ["D","D+","C","C+","B","B+"]
score = int((wScore + mScore + fScore-50)/5)
if (score < 0):
    print("Your grade is F.")
elif (score >= 80):
    print("Your grade is A.")
else:
    print("Your grade is " + str(grades[score]) + ".")