def letterAndDigit(string):
    if(string == 'none' or string == " "):
        return
    digits = []
    letters = []
    for l in string:
        if l.isdigit():
            digits.append(l)
        elif l.isalpha():
            letters.append(l)
    count = {'digit':len(digits),'letters': len(letters)}
    return count

result = letterAndDigit("There is 24 hours in 1 days")
print (result)