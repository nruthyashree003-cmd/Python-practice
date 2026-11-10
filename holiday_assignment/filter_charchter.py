target = input("Enter target string: ")
reference = input("Enter reference string: ")

result = ""

for ch in target:
    if ch not in reference:
        result += ch

print("Result:", result)