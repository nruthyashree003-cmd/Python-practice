
x = int(input("Enter an integer: "))

sign = -1 if x < 0 else 1

num = abs(x)
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

rev = rev * sign

if -2**31 <= rev <= 2**31 - 1:
    print(rev)
else:
    print(0)
