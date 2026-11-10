skills = input("Enter required skills: ").split()
n = int(input("Enter number of candidates: "))

m = len(skills)

# Assign a number to each skill
skill_index = {}

for i in range(m):
    skill_index[skills[i]] = i

# Each candidate's skills are converted into a bitmask
candidates = []

for i in range(n):
    person = input("Enter candidate skills: ").split()

    mask = 0

    for skill in person:
        if skill in skill_index:
            mask = mask | (1 << skill_index[skill])

    candidates.append(mask)

# DP stores the minimum team for each skill combination
total = 1 << m

dp = [None] * total
dp[0] = []

for i in range(n):
    for mask in range(total):
        if dp[mask] is not None:

            new_mask = mask | candidates[i]

            if dp[new_mask] is None or len(dp[new_mask]) > len(dp[mask]) + 1:
                dp[new_mask] = dp[mask] + [i]

# Print the minimum team
print("Selected candidates:", *dp[total - 1])