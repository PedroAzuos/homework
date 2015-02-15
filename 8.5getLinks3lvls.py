#8  Python: Fazer pedido http a uma pagina ler o conteudo e devolver uma lista com todos os links encontrados ( esta e para o 20)
#   *http request
#   *regular expressions
#   base: http://www.pythonforbeginners.com/code/regular-expression-re-findall

import urllib2
import re
import  os
import time

#find if log file exists. if not creates and opens it.
def logInit():
    print "Preparing log file"
    time.sleep(2)
    #generate filepath/filename based on workdir
    logFile=os.getcwd()+"\urlLog.log"
    #force new file creation if it doesn't exist
    log=open(logFile,'w+')
    log.write("")
    log.close()
    #opens file in append mode
    return open(logFile, 'a+')

"""
    #old code
    print "Finding log file"
    time.sleep(3)
    #check if log file exists
    if(os.path.isfile(logFile)):
        print "Log file found. Logging URLs"
        time.sleep(3)
        #if log file exists clear file for editing
        log=open(logFile,'w')
        log.write("")
        log.close()
        return open(logFile,'a')
    else:
        print "Log file not found. Creating log file in current work dir"
        time.sleep(3)
        #if log file does not exist, create log file
"""





#retreive links from url
def getUrl(URL):
    connection = urllib2.urlopen(URL)
    htmlData = connection.read()
    connection.close()
    links = re.findall('"((http|ftp)s?://.*?)"', htmlData)
    return links

#print links from url
def printItems(linksLvl1):

    log=logInit()

    t=0
    for item in linksLvl1:
        linksLvl2=getUrl(item)
        for item2 in linksLvl2:
            linksLvl3=getUrl(item2)
            for item3 in linksLvl3:
                t+=1
                print "Item {0}: Lvl 3: {1}".format(t,item3)
                log.write(str(item3)+"\n")
            t+=1
            print "Item {0}: Lvl 2: {1}".format(t,item2)
            log.write(str(item2)+"\n")
        t+=1
        print  "Item {0}: Lvl 1: {1}".format(t,item)
        log.write(str(item)+"\n")
    print "Total items: {0}".format(t)


tItems=0
URL = raw_input("Insert page URL to retrieve links from:")

print printItems(getUrl(URL))
