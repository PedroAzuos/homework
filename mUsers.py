# coding=utf-8
__author__ = 'Pedro'
import os, time, json, gTicket


#checks if users file JSON if exists. if not, creates file
def cUsersFile():
    #if file exists
    if os.path.exists(gTicket.usersFileName):
        print "Loading Users file"
        time.sleep(1)
        #if file not empty, load file
        if os.path.getsize(gTicket.usersFileName) > 0:
            file=open(gTicket.usersFileName, 'r+')
            #load records file
            users=json.load(file)
            file.close()
            #if any record exists return records
            if len(users)>0:
                return users
            #if file is not empty yet no records exist, load sample record to users instance.
            else:
                users = {0: "ADMIN"}
        #if file is empty, load sample record to users instance
        else:
            users = {0: "ADMIN"}
    #if file does not exist create file and load sample record to users instance
    else:
        #create new file
        file = open(gTicket.usersFileName,'w+')
        file.close()
        print "Users file empty or not found. Formatting new Users file..."
        time.sleep(1)
        #load sample user into memory to write on exit
        users = {0: "ADMIN"}
    return users

#USERS CLASS#########################################
class user:
    def __init__(self, newName):
        self.name = newName

    def saveUser(self):
        print('Adding user {0}...'.format(len(gTicket.users)))
        time.sleep(1)
        gTicket.users[len(gTicket.users)] = self.name
        gTicket.menu()

    def validateUser(self,userID):
        if userID in gTicket.users:
            return False
        else:
            print "User does not exist. Insert a valid user"


