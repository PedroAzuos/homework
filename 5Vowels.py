#5  Python: funcao que receba um caracter e que retorne True se for uma vogal, False se for outra coisa

aVowels = ["a","e","i","o","u"]

def checkVowel(cChar):
    bCheck = False #parece pouco elegante
    for item in aVowels:
        if(item == cChar):
            bCheck = True
            break
        else:
            bCheck = False
    return bCheck
cChar = raw_input("Insert character").lower() #input() n funciona pq

print checkVowel(cChar)