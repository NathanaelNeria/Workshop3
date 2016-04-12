import string

MIN_PASSWORD_LENGHT=5
MAX_PASSWORD_LENGHT=15
LOWER=string.ascii_lowercase
UPPER=string.ascii_uppercase
DIGITS=string.digits
PUNCTUATION=string.punctuation
lower=0
upper=0
digit=0
punctuation=0
print("Please enter a valid password")
password=input("Your password must be between 5 and 15 characters, and contain: \n    1 or more uppercase characters \n    1 or more lowercase characters \n    1 or more numbers   \n    and 1 or more special characters:	!@#$%^&*()_-­‐=+`~,./o'[]\<>?O{}| \n >")
for each in password:
    if each in LOWER:
        lower=lower+1
    elif each in UPPER:
        upper=upper+1
    elif each in DIGITS:
        digit=digit+1
    elif each in PUNCTUATION:
        punctuation=punctuation+1
while len(password)<MIN_PASSWORD_LENGHT or len(password)>MAX_PASSWORD_LENGHT or lower<1 or upper<1 or digit<1 or punctuation<1:
    print("Invalid password!")
    password=input(">")
    lower = 0
    upper = 0
    digit = 0
    punctuation = 0
    for each in password:
        if each in LOWER:
            lower=lower+1
        elif each in UPPER:
            upper=upper+1
        elif each in DIGITS:
            digit=digit+1
        elif each in PUNCTUATION:
            punctuation=punctuation+1
print("Password accepted")
