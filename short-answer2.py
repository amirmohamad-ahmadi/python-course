val = int(input())
if val < 10:
    if val != 5:
        print("WOW", end='')
    else:
        val += 1
else:
    if val == 17:
        val += 10
    else:
        print("WHOA", end='')

print(val)



# choose one of these numbers as your input : 3 , 21 , 5 , 17 , -5
# if you write 3 outpot is going to be wow3
# if you write 21 outpot is going to be whoa21
# if you write 5 outpot is going to be 6
# if you write 17 outpot is going to be 27
# if you write -5 outpot is going to be wow-5


