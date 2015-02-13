#5  Python: funcao que receba um caracter e que retorne True se for uma vogal, False se for outra coisa

aVowels = ["a","e","i","o","u"]

def checkVowel(cChar):
    bCheck = False
    for item in aVowels:
        if(item == cChar):
            return True
    return False

cChar = raw_input("Insert character").lower()

print checkVowel(cChar)