# write a python function called "summarize_grades" that accept a student's names as a mandatory argument and an arbitrary numbers of grade  the function should,  
# 1. Print the student's names 
# 2. Calculate and print the highest grade, lowest grade and the average garde from the provided scores.
# 3. If no grade are provided you should print "no grade available"

def summarize_grades(student_name, *grades):
    print("Student name: ",student_name)

    if grades:
        highest_grade = max(grades) 
        lowest_grade = min(grades) 
        average_grade = sum(grades) / len(grades) 
        print(f"Highest Grade: {highest_grade}") 
        print(f"Lowest Grade: {lowest_grade}") 
        print(f"Average Grade: {sum(grades)/len(grades)}") 

    else: 
        print("No grades available")

summarize_grades("Aravinda",20,40,50,30,80) #Student name:  Aravinda
                                            #Highest Grade: 80
                                            #Lowest Grade: 20
                                            #Average Grade: 44.0

summarize_grades("Aravinda") #No grades available
summarize_grades() #TypeError: summarize_grades() missing 1 required positional argument: 'student_name'