lower = 10
upper = 100
lowercase=int(input("Enter a number({}-{}):".format(lower,upper)).strip())
uppercase=int(input("Enter a number({}-{}):".format(lower,upper)).strip())
for i in range(lowercase,uppercase):
    print("{} {}".format(i, chr(i)))