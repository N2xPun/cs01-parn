def sInput(min,max,text):
    outScore = -1
    while(outScore < min or outScore > max):
        outScore = int(input("Please enter your " + str(text) + " score: "))
    return outScore
wScore = sInput(0,30,"work")
mScore = sInput(0,30,"midterm")
fScore = sInput(0,40,"final")
grades = ["F","F","F","F","F","F","F","F","F","F","D","D+","C","C+","B","B+","A","A","A","A"]
score = int((wScore + mScore + fScore)/5)
print("Your grade is " + str(grades[score]) + ".")