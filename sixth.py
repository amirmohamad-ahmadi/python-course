sum = 0
for x in range(20):
    a = float(input(' please enter a number : '))
    sum += a

    if(x == 0):
        min = a
        max= a
    else:
        if(a > max):
            max = a
        if(a < min):
            min = a
    

avg = sum / 20
print('avg =',avg,' min =' , min , ' max =' , max)

input()
        