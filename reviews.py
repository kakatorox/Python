from functools import reduce
numero=(2,4,3,1)
def suma(x,y):
    return x+y
sumar=reduce(suma,numero)
print(sumar)
