# A function to average six grade components
def calculateGrade(lab, hw, rd, lect, midterm, final):
 average = (lab* 0.15 + hw *0.15 + rd *0.10+ lect *0.10 + midterm *0.25+ final *0.25) 
 return average
# The code below will test the calculateGrade function
if __name__ == "__main__":
 result = calculateGrade(100, 90, 100, 90, 79, 84)
 print("Your overall grade is", result)