#6  Python: definir uma funccaoo que faca reverse a uma string: ex: "pedro" -> "ordep"

def reverse(cString):
    return cString[::-1]

cString = raw_input("Insert string to reverse")

print(reverse(cString))