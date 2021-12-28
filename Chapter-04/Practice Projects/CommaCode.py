def commaCode(x):
    commaCode = ''
    n = len(x)
    for i in x[0:n-1]:
        commaCode += str(i)+', '
    commaCode+= 'and '+ str(x[-1]) + '.'
    return commaCode

spam = list(input().split())
print(commaCode(spam))