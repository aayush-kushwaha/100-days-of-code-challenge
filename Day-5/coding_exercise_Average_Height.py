student_heights = input("Input a list of Student Heights: ").split() #The split() method splits a string into a list
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n]) #You can’t convert an entire list into an integer so here loop has been used. 
                                            #You have to get an index from the list and convert that into an integer. Just like this.
                                            #That's the reason why student_heights[n] = int(student_heights[n]) is written
total_height = 0
for height in student_heights:
    total_height = total_height + height
print(f"The total height of the Students is {total_height}")

no_of_students = 0
for student in student_heights:
    no_of_students = no_of_students + 1
print(f"The number of students are: {no_of_students}")

average_height = round(total_height/no_of_students)
print(f"The average height of Students are: {average_height}")