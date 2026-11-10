import csv
import json

data = """name,age,salary,join_date
John,25,45000,2023-01-15
 Alice , 30 , 55000 , 2022-05-10
David, ,60000,2021-03-20
Priya,28,Unknown,2023-07-12
Sam,abc,40000,2022-11-05
Ravi,32,65000,2020-06-18
"""

lines = data.splitlines()

reader = csv.DictReader(lines)

cleaned_records = []

for row in reader:

    # Remove extra spaces
    name = row["name"].strip()
    age = row["age"].strip()
    salary = row["salary"].strip()
    join_date = row["join_date"].strip()

    # Skip missing or invalid values
    if age == "" or salary == "" or salary == "Unknown":
        continue

    try:
        age = int(age)
        salary = float(salary)

    except ValueError:
        continue

    # Create a clean employee dictionary
    employee = {
        "name": name,
        "age": age,
        "salary": salary,
        "join_date": join_date
    }

    cleaned_records.append(employee)

# Write data into JSON file
with open("cleaned_data.json", "w") as file:
    json.dump(cleaned_records, file, indent=2)

print("Cleaned Records:")
print(cleaned_records)

print("JSON file created successfully!")