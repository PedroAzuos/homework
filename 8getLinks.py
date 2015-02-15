#8  Python: Fazer pedido http a uma pagina ler o conteudo e devolver uma lista com todos os links encontrados ( esta e para o 20)
#   *http request
#   *regular expressions
#   base: http://www.pythonforbeginners.com/code/regular-expression-re-findall

import urllib2
import re

#retreive links from url
def getUrl(URL):
    connection = urllib2.urlopen(URL)
    htmlData = connection.read()
    return re.findall('"((http|ftp)s?://.*?)"', htmlData)

#print links from url
def printItems(links):
    i=0
    for item in links:
        print links[i].__getitem__(0)
        i+=1

URL = raw_input("Insert page URL to retrieve links from:")

print printItems(getUrl(URL))