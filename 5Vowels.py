#5  Python: funcao que receba um caracter e que retorne True se for uma vogal, False se for outra coisa

aVowels = ["a","e","i","o","u","A","E","I","O","U"]


def checkVowel(cChar):
#   bCheck = False
    for item in aVowels:
        if(item==cChar):
            return True
        else:
            return False

cChar = raw_input("Insert character") #porque é que aqui tive de usar raw input em vez de input? já li que retorna cenas diferentes mas não percebi a diferença

print checkVowel(cChar)