# coding=utf-8
__author__ = 'Pedro'

import mUsers
import mTickets
import json, os, time, imp
ticketsFileName = os.getcwd() + "\Tickets.log"
usersFileName = os.getcwd() + "\Users.log"
#mTickets = imp.load_source('mTickets', os.getcwd()+"\mTickets.py")
#mUsers = imp.load_source('musers', os.getcwd()+"\mTickets.py")


def saveUsers():
    with open(usersFileName, 'w+') as outfile:
            json.dump(users, outfile)
    print "Users saved."
    time.sleep(1)

def saveTickets():
    with open(ticketsFileName, 'w+') as outfile:
            json.dump(tickets, outfile)
    print "Tickets saved."
    time.sleep(1)




def addUser():
    newUserName = raw_input("Insert new user name")
    newUser = mUsers.user(newUserName)
    newUser.saveUser(users,ID=len(users))
    saveUsers()


def newTicket():
    print("Creating new ticket")
    userID = raw_input("Insert user ID to assign the ticket")
    while True:
        targetUser = mUsers.user("validationUser")
        validation = targetUser.validateUser(userID, users)
        if validation == False:
            openTicket(userID)
            break
        else:
            print 'Invalid user selected'
            break

def openTicket(userID):
    userID=userID
    title = raw_input("Insert the ticket Title")
    description = raw_input("Insert the ticket Description")
    newTicket = mTickets.ticket(userID,title,description)
    newTicket = newTicket.addTicket(newID=len(tickets))
    tickets.append(newTicket)
    saveTickets()

def viewTicket():
    ticketID = raw_input("Insert ticket ID")
    for item in tickets:
        if item["ticketID"]==int(ticketID):
            print "Ticket ID:{0}".format(item["ticketID"])
            print "Ticket Title:{0}".format(item["title"])
            print "Ticket Description:{0}".format(item["description"])
            print "Ticket Status:{0}".format(item["status"])

    option = raw_input("1 - Main Menu \n 2 - Change Ticket Status")

    if option == "1":
        menu()
    elif option == "2":
        mTickets.changeTicketStatus(ticketID, tickets) #CONFIRMAR SE ESTÁ A FUNCIONAR#############################
    else:
        print("No valid option selected.")
        time.sleep(1)


def listTickets():
        userID=raw_input("Insert user ID")
        print "Tickets assigned to user {0}:".format(userID)
        for item in tickets:
            if item["userID"]==userID:
                print "Ticket {0}".format(item["ticketID"])

        option = raw_input("1 - Edit Ticket \n 2 - Main Menu")

        if option == "1":
            viewTicket()
        else:
            return

def menu():
    while True:
        option = raw_input("Ticket Manager: \n 1 - Open Ticket \n 2 - List Tickets \n 3 Create user")

        if option <> 1 and 2 and 3 and 4:
                if option == "1":
                    newTicket()
                elif option == "2":
                    listTickets()
                elif option == "3":
                    addUser()
                elif option == "4":
                    mUsers.user.viewUser(1,users)
                else:
                    print "Closing app"
                    time.sleep(1)
        else:
            print 'Closing...'




#prepare users and tickets files
users = mUsers.cUsersFile()
tickets = mTickets.cTicketsFile()

#enter menu
menu()

