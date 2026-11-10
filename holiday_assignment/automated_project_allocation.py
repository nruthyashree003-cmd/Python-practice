
import sys
import random
import math
from collections import defaultdict
from itertools import combinations
from functools import reduce
from datetime import datetime

# Student details: name, department, marks
students = [
    ("Anita", "CSE", 85),
    ("Rahul", "CSE", 78),
    ("Priya", "CSE", 92),
    ("Kiran", "CSE", 80),

    ("Arun", "AI", 88),
    ("Meena", "AI", 90),
    ("Ravi", "AI", 75),

    ("Sneha", "Data Science", 95),
    ("Vijay", "Data Science", 82),
    ("Pooja", "Data Science", 87),

    ("Ajay", "Cyber Security", 79),
    ("Divya", "Cyber Security", 91)
]

# 1. Get team size from command line
if len(sys.argv) != 2:
    print("Usage: python allocation.py 3")
    sys.exit()

team_size = int(sys.argv[1])

if team_size <= 0:
    print("Team size must be greater than zero.")
    sys.exit()

# 2. Group students by department
departments = defaultdict(list)

for name, department, marks in students:
    departments[department].append((name, marks))

# 3. Generate possible teams
all_teams = []

for department, members in departments.items():
    possible_teams = list(combinations(members, team_size))

    for team in possible_teams:
        all_teams.append((department, team))

if not all_teams:
    print("No team can be formed with the given team size.")
    sys.exit()

# 4. Randomly select one team
department, selected_team = random.sample(all_teams, 1)[0]

# 5. Calculate total marks using reduce()
marks = [student[1] for student in selected_team]

total = reduce(lambda a, b: a + b, marks)

# 6. Calculate average using math
average = math.fsum(marks) / team_size

# 7. Get allocation date
allocation_date = datetime.now().strftime("%d-%m-%Y")

# Display result
print("\n===== PROJECT TEAM ALLOCATION =====")
print("Team Size:", team_size)
print("Allocation Date:", allocation_date)
print("Department:", department)

print("\nSelected Team:")

for i, (name, mark) in enumerate(selected_team, start=1):
    print(i, ".", name, "-", mark)

print("Total Marks:", total)
print("Average Marks:", format(average, ".2f"))
