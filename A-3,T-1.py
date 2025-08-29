def factorieal(n):
    if n<0:
        return ('NOT VALID INPUT')
    elif n<2:
        return 1
    else:
        return n*(factorieal(n-1))
x=int(input('Enter a number: '))
y=factorieal(x)
print('Factorial of' ,x,' is ',y)