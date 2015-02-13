#3  Python: definir uma funcaoo max() que aceita 2 argumentos e que devolve o numero maior
def max(A,B):
    if A>B:
        return "{} > {}" .format(A, B)

    else:
        return "{} > {}" .format(B, A)

print "Comparing two values:"
A = input("Insert value A")
B = input("Insert value B")

print "Comparison Result: ", str(max(A,B))