#---------------------------IF---------------------------#
if 45 > 10:
    print("45 is greater than 10")
    print("This is a simple if statement")
    print("True")
else:
    print("This is a simple else statement")
    print("False")



    
if 45 > 100:
    print("45 is greater than 10") #This will not be printed because the condition is false
    
#---------------------------ELSE IF---------------------------#
score=74
if score >= 90:
    print("Congratulations! You got an A grade")
elif score >= 80:
    print("Congratulations! You got a B grade")
elif score >= 70:
    print("Congratulations! You got a C grade")
else:
    print("Congratulations! You got a D grade")