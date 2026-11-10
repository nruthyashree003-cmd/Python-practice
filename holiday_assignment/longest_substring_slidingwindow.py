s = input("Enter a string: ")

visited = [False] * 26

left = 0
max_length = 0

for right in range(len(s)):

    index = ord(s[right]) - ord('a')

    while visited[index]:
        left_index = ord(s[left]) - ord('a')
        visited[left_index] = False
        left += 1

    visited[index] = True

    length = right - left + 1

    max_length = max(max_length, length)

print("Length of the longest unique substring:", max_length)