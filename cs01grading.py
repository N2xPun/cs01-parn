wScore = int(input("Please enter your work score: "))
mScore = int(input("Please enter your midterm score: "))
fScore = int(input("Please enter your final score: "))

score = wScore + mScore + fScore

if (score >= 80 and score <= 100):
    print("Your grade is A.")
elif (score <= 79 and score >= 75):
    print("Your grade is B+.")
elif (score <= 74 and score >= 70):
    print("Your grade is B.")
elif (score <= 69 and score >= 65):
    print("Your grade is C+.")
elif (score <= 64 and score >= 60):
    print("Your grade is C.")
elif (score <= 59 and score >= 55):
    print("Your grade is D+.")
elif (score <= 54 and score >= 50):
    print("Your grade is D.")
elif (score <= 49 and score >= 0):
    print("Your grade is F.")
else:
    print("Your score is invalid.")