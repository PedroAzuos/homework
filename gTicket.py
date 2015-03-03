# coding=utf-8
__author__ = 'Pedro'

import mTickets, mUsers, json, os, time

ticketsFileName = os.getcwd() + "\Tickets.log" # this belongs to the ticket class
usersFileName = os.getcwd() + "\Users.log"     # this belong to the users class


# this method can be a static method on the users class where you pass the user list as parameter
def saveUsers():
    with open(usersFileName, 'w+') as outfile:
            json.dump(users, outfile)
    print "Users saved."
    time.sleep(1)

# same as above but for the tickets
def saveTickets():
    with open(ticketsFileName, 'w+') as outfile:
            json.dump(tickets, outfile)
    print "Tickets saved."
    time.sleep(1)

def addUser():
    newUserName = raw_input("Insert new user name")
    newUser = mUsers.user(newUserName)
    newUser.saveUser()
    menu()


def openTicket():
    print("Creating new ticket")
    userID = raw_input("Insert user ID to assign the ticket")
    while True:
        targetUser = mUsers.user("validationUser")
        validation = targetUser.validateUser(userID)
        if validation == False:
            break
        else:
            openTicket()
    title = raw_input("Insert the ticket Title")
    description = raw_input("Insert the ticket Description")
    newTicket = mTickets.ticket(userID,title,description)
    newTicket.addTicket()
    menu()

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
        mTickets.changeTicketStatus(ticketID)
    else:
        print("No valid option selected.")
        time.sleep(1)
        menu()


def listTickets():
        userID=raw_input("Insert user ID")
        print "Tickets assigned to user {0}:".format(userID)
        for item in tickets:
            if item["userID"]==userID:
                print "Ticket {0}".format(item["ticketID"])

        option = raw_input("1 - Edit Ticket \n 2 - Main Menu")

        if option == "1":
            viewTicket()
        elif option == "2":
            menu()
        else:
            print("No valid option selected.")
            time.sleep(1)
            menu()

def menu():
    option = raw_input("Ticket Manager: \n 1 - Open Ticket \n 2 - List Tickets \n 3 Create user \n 4 Save and Exit")

    if option == "1":
        openTicket()
    elif option == "2":
        listTickets()
    elif option == "3":
        addUser()
    else:
        print "Saving and exiting"
        time.sleep(1)

#prepare users and tickets files
tickets = mTickets.cTicketsFile()
users = mUsers.cUsersFile()

#enter menu
menu()

#save tickets and files after exiting menu (exiting program)
saveTickets()
saveUsers()
