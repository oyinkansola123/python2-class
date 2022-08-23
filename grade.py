gradeA=5
gradeB=4
gradeC=3
gradeD=2
gradeE=1
englishunit=4
mathsunit=4
biologyunit=3
physicsunit=2
chemistryunit=1
totalunit=(englishunit + mathsunit + biologyunit + physicsunit + chemistryunit)
# totalunit=(14)
print("enter marks for 5 courses")

english=int(input("enter the score of STA 313"))

if english>=75 and english<=100:
    gradeEN=gradeA
elif english>=65 and english<70:
    gradeEN=gradeB
elif english>=55 and english<=60:
    gradeEN=gradeC
elif english>=45 and english<=50:
    gradeEN=gradeD
elif english>=35 and english<40:
    gradeEN=gradeE
print(gradeEN)

maths=int(input("enter the score of STA 311"))
if maths>=75 and maths<=100:
    gradeM=gradeA
elif maths>=65 and maths<70:
    gradeM=gradeB
elif maths>=55 and maths<=60:
    gradeM=gradeC
elif maths>=45 and maths<=50:
    gradeM=gradeD
elif maths>=35 and maths<40:
    gradeM=gradeE
print(gradeM)

physics=int(input("enter the score of STA 321"))
if physics>=75 and physics<=100:
    gradePHY=gradeA
elif physics>=65 and physics<70:
    gradePHY=gradeB
elif physics>=55 and physics<=60:
    gradePHY=gradeC
elif physics>=45 and physics<=50:
    gradePHY=gradeD
elif physics>=35 and physics<40:
    gradePHY=gradeE
print(gradePHY)

chemistry=int(input("enter the score of STA 361"))
if chemistry>=75 and chemistry<=100:
    gradeCHM=gradeA
elif chemistry>=65 and chemistry<70:
    gradeCHM=gradeB
elif chemistry>=55 and chemistry<=60:
    gradeCHM=gradeC
elif chemistry>=45 and chemistry<=50:
    gradeCHM=gradeD
elif chemistry>=35 and chemistry<40:
    gradeCHM=gradeE
print(gradeCHM)

biology=int(input("enter the score of STA 331"))
if biology>=75 and biology<=100:
    gradeBIO=gradeA
elif biology>=65 and biology<70:
        gradeBIO=gradeB
elif biology>=55 and biology<=60:
    gradeBIO=gradeC
elif biology>=45 and biology<=50:
    gradeBIO=gradeD
elif biology>=35 and biology<40:
    gradeBIO=gradeE
print(gradeBIO)
score=((gradeEN*englishunit))+((gradeM*mathsunit))+((gradeCHM*chemistryunit))+((gradeBIO*biologyunit))+((gradePHY*physicsunit))
cgpa=(score)/(totalunit)
print(cgpa)

# englishunit=4
# mathsunit=4
# biologyunit=3
# physicsunit=2