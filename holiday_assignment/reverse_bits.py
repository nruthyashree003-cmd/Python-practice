n = int(input("Enter a number: "))

# Convert the number into a 32-bit binary string
binary = format(n, '032b')

# Reverse the binary string
reversed_binary = binary[::-1]

# Convert the reversed binary string back to decimal
result = int(reversed_binary, 2)

print("Reversed Bits:", result)