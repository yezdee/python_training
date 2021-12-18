student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

counter = 0
total = 0
for heights in student_heights:
    total = heights + total
    counter = counter + 1
print (round(total/counter))
