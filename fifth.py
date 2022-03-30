def sezar(text,s):
    result = ""

    for m in text:
    
        if ( 'A'<=ch <= 'Z'):
            result += chr((ord(ch) + s-65) % 26 + 65)
 
        else:
            result += chr((ord(ch) + s - 97) % 26 + 97)
 
    return result
 

text = input(' please enter a text : ')
s = int(input('enter shift count: '))
print ("res: " + sezar(text,s))

input()