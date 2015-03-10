# coding=utf-8
__author__ = 'Pedro'
__name__ = 'mUsers'
import os, time, json

usersFileName = os.getcwd() + "\Users.log"

#checks if users file JSON if exists. if not, creates file
def cUsersFile():
    #if file exists
    if os.path.exists(usersFileName):
        print "Loading Users file"
        time.sleep(1)
        #if file not empty, load file
        if os.path.getsize(usersFileName) > 0:
            file=open(usersFileName, 'r+')
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
        file = open(usersFileName,'w+')
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

    def saveUser(self,users, ID):
        users=users
        print('Adding user {0}...'.format(ID))
        time.sleep(1)
        users[ID] = self.name
        return True


    def validateUser(self,userID, users):
        users=users
        if userID in users:
            return False
        else:
            print "User does not exist. Insert a valid user"


    def viewUser(self,userID, users):
        users=users
        if userID in users:
            print users[userID]["name"]
        else:
            print "User does not exist. Insert a valid user"