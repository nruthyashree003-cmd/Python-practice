s = input("Enter a string: ")

left = 0
max_length = 0
seen = set()

for right in range(len(s)):

    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    length = right - left + 1

    max_length = max(max_length, length)

print("Length of the longest unique substring:", max_length)