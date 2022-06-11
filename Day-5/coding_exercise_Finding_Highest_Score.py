'''
You are going to write a program that calculates the highest score from a List of scores.
e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
Important you are not allowed to use the max or min functions. The output words must match the example. i.e
The highest score in the class is: x
'''
students_score = input("Input student's score separated by comma: ").split() #.split() method splits a string a 
for n in range(0,len(students_score)):            
    students_score[n] = int(students_score[n]) 
print(students_score)

highest_score = 0 
for score in students_score:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")