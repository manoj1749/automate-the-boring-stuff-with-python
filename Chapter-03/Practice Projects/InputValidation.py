#collatz sequence with input validation
def collatzseq(n):
    while n!=1:
        if n%2==0:
            n = n//2
        else:
            n = (3*n)+1
        print(n)
x = 0
while x==0:
    print('Enter number:')
    try:
        n = int(input())
        x+=1
    except ValueError:
        print('Error: Given argument is invalid, Only integers')
collatzseq(n)
