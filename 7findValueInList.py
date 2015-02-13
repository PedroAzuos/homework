#7  Python: definir uma funcaoo que receba um valor e uma lista e determina se o valor pertence a lista

#find if value exists in list of value
def findValue(vList,sValue):
    for item in vList:
        if item == sValue:
            return True
    return False
#get list of values from user
vList=[0]
def getvList():
    print "Receiving list of values"
    i =0
    while True:
        i += 1
        vInput = raw_input("Insert value {0}. Press enter again to finish.".format(i))
        vList.append(vInput)
        if vList[i]== "":
            break
    return vList

print getvList()

#get value to look for from user
sValue = "b"

print findValue(vList,sValue)