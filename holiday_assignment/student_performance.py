import random
from datetime import date
from collections import Counter
from functools import reduce

students = {
    "Tarun": [82, 91, 78],
    "Karthik": [65, 72, 68],
    "Chadrika": [91, 95, 89],
    "Trisha": [76, 81, 79],
    "Atul": [88, 84, 92]
}

# 1. Calculate average marks
averages = {}

for name, marks in students.items():
    averages[name] = sum(marks) / len(marks)

print("Student Averages:")
for name, avg in averages.items():
    print(name, ":", avg)

# 2. Find highest average
topper = max(averages, key=averages.get)

print("\nHighest Average:", topper)
print("Average Marks:", averages[topper])

# 3. Randomly select one student
selected = random.choice(list(students.keys()))
print("\nRandomly Selected Student:", selected)

# 4. Display current date
print("\nCurrent Date:", date.today())

# 5. Classify grades using Counter
grades = []

for avg in averages.values():
    if avg >= 90:
        grades.append("A")
    elif avg >= 75:
        grades.append("B")
    elif avg >= 60:
        grades.append("C")
    else:
        grades.append("D")

grade_count = Counter(grades)

print("\nGrade Classification:", grade_count)

# 6. Calculate total marks using reduce()
all_marks = []

for marks in students.values():
    all_marks.extend(marks)

total = reduce(lambda a, b: a + b, all_marks)

print("\nTotal Marks:", total)