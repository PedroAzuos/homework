#4  Python: definir uma funcao max() que aceite um numero indeterminado de argumentos (este e para o 20)
import sys
def max(*n):
    iMax = -sys.maxint-1
    for item in n:
        if item>iMax:
            iMax=item
    return iMax

print "max(*n) Method:"
print max(1, 56 ,78, 8,7, 8)
print max(12, 254)
