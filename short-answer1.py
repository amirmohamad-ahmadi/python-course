i = int(input(" write a number : "))
j = int(input(" write a number : "))
k = int(input(" write a number : "))
# choose your number from a,b,c,d,e,f in asked numbers part
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k :
        j = i
    else:
        i = k

print(" i = ", i, " j = ", j, " k = ", k)

# asked numbers:
# a) = input : i = 3 , j = 5 , k = 7 
# b) = input : i = 3 , j = 7 , k = 5 
# c) = input : i = 5 , j = 3 , k = 7 
# d) = input : i = 5 , j = 7 , k = 3 
# e) = input : i = 7 , j = 3 , k = 5 
# f) = input : i = 7 , j = 5 , k = 3 

# outpot of asked numbers :
# a) output : i = 5 , j = 5 , k = 7
# b) output : i = 3 , j = 5 , k = 5
# c) output : i = 7 , j = 3 , k = 7
# d) output : i = 5 , j = 3 , k = 3
# e) output : i = 5 , j = 3 , k = 5
# f) output : i = 7 , j = 7 , k = 3
