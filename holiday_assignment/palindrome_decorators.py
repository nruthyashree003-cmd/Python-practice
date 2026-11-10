def palindrome_decorator(func):

    def wrapper(num):
        reverse = int(str(num)[::-1])

        if num == reverse:
            print(num, "is a Palindrome")
        else:
            print(num, "is Not a Palindrome")

    return wrapper


@palindrome_decorator
def check_palindrome(num):
    pass


num = int(input("Enter a number: "))
check_palindrome(num)