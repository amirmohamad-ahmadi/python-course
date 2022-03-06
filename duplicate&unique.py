a = int(input(" write a number : "))
b = int(input(" write a number : "))
c = int(input(" write a number : "))
d = int(input(" write a number : "))
e = int(input(" write a number : "))


if a == b or a == c or a == d or a == e:
    print(" DUPLICATE ")

elif b == c or b == d or b == e or c == d or c == e or d == e:
    print(" DUPLICATE ")

else: print(" ALL UNIQUE ")