#program to calculate the factorial of a number

#let as consider a = 19

def fact(f):
    if f == 1 or f == 0:
        return 1
    else:
        return f*fact(f - 1)

a = 5
print("the factorial is :",fact(a))
