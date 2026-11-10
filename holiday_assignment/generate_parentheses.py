def generate(n, result, current, open_count, close_count):

    if len(current) == 2 * n:
        result.append(current)
        return

    if open_count < n:
        generate(n, result, current + "(", open_count + 1, close_count)

    if close_count < open_count:
        generate(n, result, current + ")", open_count, close_count + 1)


n = int(input("Enter number of pairs: "))

result = []

generate(n, result, "", 0, 0)

print("Valid combinations:")
print(result)