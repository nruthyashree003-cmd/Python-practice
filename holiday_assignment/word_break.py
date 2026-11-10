s = input("Enter the string: ")

word_dict = input("Enter dictionary words separated by spaces: ").split()
word_set = set(word_dict)

memo = {}

def word_break(start):

    if start == len(s):
        return [""]

    if start in memo:
        return memo[start]

    result = []

    for end in range(start + 1, len(s) + 1):

        word = s[start:end]

        if word in word_set:

            remaining = word_break(end)

            for part in remaining:
                if part == "":
                    result.append(word)
                else:
                    result.append(word + " " + part)

    memo[start] = result
    return result


answers = word_break(0)

if answers:
    print("Can Segment: True")
    print("Segmentations:")

    for answer in answers:
        print(answer)
else:
    print("Can Segment: False")