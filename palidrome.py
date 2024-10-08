def main():
    test = str(input("Potential Palindrome: "))
    lowercase = test.lower()
    simple_string = ''.join([*filter(str.isalnum, lowercase)])
    backwards_string = simple_string[::-1]
    
    if simple_string == backwards_string:
        print(f"{test} is a palindrome")
    else:
        print(f"'{test}' is not a palindrome")

main()