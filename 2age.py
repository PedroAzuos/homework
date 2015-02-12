import datetime

dCurrentDate = datetime.datetime.now()

iAge = input("Insert age")
iMonth = input("Insert month of birth")
iNewDate = dCurrentDate.year-iAge

print "Born in: {}-{}".format(iMonth, iNewDate)