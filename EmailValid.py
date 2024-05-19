import re
email_condition=r"^[a-z]+[\_]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your Email: ")

#now to check user_email satisfy the condition or not 
if re.search(email_condition,user_email):
    print("Valid Email: ")
else:
    print("Invalid Email")    


#^: Asserts the start of the string.
#[a-z]+: Matches one or more lowercase letters from a to z.
#[\_]?: Optionally matches an underscore _.
#[a-z0-9]+: Matches one or more lowercase letters or digits.
#[@]: Matches the "@" symbol.
#\w+: Matches one or more word characters (letters, digits, or underscores) for the domain name.
#[.]: Matches the dot "." symbol.
#\w{2,3}: Matches 2 or 3 word characters for the top-level domain (e.g., "com", "org").