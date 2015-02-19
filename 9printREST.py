# coding=utf-8
import urllib2
import json


def getRestData(url):
    request = urllib2.urlopen(url)

    rData = json.load(request)
    return rData

"""
    #old code. redundant lol.

    mainData = rData["main"]
    coord = rData["coord"]
    sys = rData["sys"]
    weather = rData["weather"]
    wind = rData["wind"]
    clouds = rData["clouds"]
    name = rData["name"]
    return {"mainData": mainData,"coord": coord,"sys": sys, "weather":weather, "wind":wind,"clouds": clouds, "name": name}
"""

def printData(rData):
    return 0





url = str("http://api.openweathermap.org/data/2.5/weather?q=Lisbon,pt&lang=pt&units=metric")

restData = getRestData(url)

print "The weather in {0} is {1}. The current temperature is {2}º with a {3}º max and a {4}º min"\
    .format(restData["name"],
            restData["weather"][0]["main"],
            restData["main"]["temp"],
            restData["main"]["temp_max"],
            restData["main"]["temp_min"]
)
