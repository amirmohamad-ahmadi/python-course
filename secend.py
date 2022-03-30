def bmm(a , b):
    if(b == 0):
        return a
    return bmm(b , a % b)




a = int(input(' please enter a number: '))

b = int(input(' please enter a number: '))

print('bmm = ' , bmm(a , b))

input()