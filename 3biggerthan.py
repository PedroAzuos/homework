#3  Python: definir uma funcaoo max() que aceita 2 argumentos e que devolve o numero maior
def max(A,B):
    if A>B:
        print "A:",A," > B:",B
        input()
    else:
        print "B:",B," > A:",A

print "Comparing two values:"
A = input("Insert value A")
B = input("Insert value B")

max(A,B)