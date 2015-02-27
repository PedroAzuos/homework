# coding=utf-8
import os, time, json

usersFileName = os.getcwd() + "\Users.log"
ticketsFileName = os.getcwd() + "\Tickets.log"

# TICKETSCLASS#######################################
class ticket:
    def __init__(self, userID, title, description):
        self.userID = userID
        self.title = title
        self.description = description

    #returns tickets file if exists. if not, creates file
    def cTicketsFile(self):
        print "Loading Tickets file"
        time.sleep(1)
        file=open(ticketsFileName).read()
        #if file is empty, format in JSON and add sample ticket
        if  file == "":
            print "No file detected. Creating Tickets file..."
            time.sleep(1)
            data = [{"ticketID": 0, "userID": "0", "title": "Sample Title", "description": "Sample Description",
                     "status": "Open"}]
            with open(ticketsFileName,'w') as outfile:
                json.dump(data, outfile)

        #return open file
        file = open(ticketsFileName, 'r')
        return file

    def saveTicket(self):
        #load/prepare user file
        self.cTicketsFile()
        tickets = json.load(open(ticketsFileName))
        print('Adding ticket {0}...'.format(len(tickets)))
        time.sleep(1)
        #adds new record. ID is JSON length (always 1 bigger by default)
        newID=len(tickets)
        data = {"ticketID": newID,
                "userID": self.userID,
                "title": self.title,
                "description": self.description,
                "status": "Open"}

        tickets.append(data)

        with open(ticketsFileName, 'w+') as outfile:
            json.dump(tickets, outfile)
        menu()

    def listTickets(self,userID):
        tickets = json.load(open(ticketsFileName))

    def openTicket(self,ticketID):
        tickets = json.load(open(ticketsFileName))

    def changeTicketStatus(self,ticket):
        tickets = json.load(open(ticketsFileName))


def listTickets():
        tickets = json.load(open(ticketsFileName))
        userID=raw_input("Insert user ID")
        print "Tickets assigned to user {0}:".format(userID)
        for item in tickets:
            if item["userID"]==userID:
                print "Ticket {0}".format(item["ticketID"])

        option = raw_input("1 - Edit Ticket \n 2 - Main Menu")

        if option == "1":
            editTicket()
        elif option == "2":
            menu()
        else:
            print("No valid option selected.")
            time.sleep(1)
            menu()

def editTicket():
    ticketID = raw_input("Insert ticket ID")
    file = open(ticketsFileName,'r')
    tickets = json.load(file)
    file.close()
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
        changeTicketStatus(ticketID)
    else:
        print("No valid option selected.")
        time.sleep(1)
        menu()

def changeTicketStatus(ticketID):
    file = open(ticketsFileName)
    tickets = json.load(file)
    file.close()

    for item in tickets:
        if item["ticketID"]==int(ticketID):
            if item["status"]=="Open":
                print "Ticket closed"
                time.sleep(1)
                item["status"]="Closed"
            else:
                print "Ticket re-opened"
                time.sleep(1)
                item["status"]="Open"

    with open(ticketsFileName, "w") as outfile:
                json.dump(tickets, outfile)
    editTicket()


def openTicket():
    print("Creating new ticket")
    userID = raw_input("Insert user ID to assign the ticket")
    while True:
        targetuser = user("validationUser")
        validation = targetuser.validateUser(userID)
        if validation == False:
            break
        else:
            openTicket()
    title = raw_input("Insert the ticket Title")
    description = raw_input("Insert the ticket Description")
    newTicket = ticket(userID,title,description)
    newTicket.saveTicket()
    menu()





#USERSCLASS#########################################
class user:
    #add static var for ID generator
    #add new static method to get new id


    def __init__(self, newName):
        self.name = newName

    #returns users file JSON if exists. if not, creates file
    def cUsersFile(self):
        print "Loading Users file"
        time.sleep(1)

        file=open(usersFileName).read()
        #if file is empty, format in JSON and add sample ticket
        if  file == "":
            print "No file detected. Creating Users file..."
            time.sleep(1)
            data = {0: "ADMIN"}
            with open(usersFileName, "w") as outfile:
                json.dump(data, outfile)

        #return open file
        file = open(usersFileName, 'r')
        return file

    def saveUser(self):
        #load/prepare user file
        self.cUsersFile()
        users = json.load(open(usersFileName))

        print('Adding user {0}...'.format(len(users)))
        time.sleep(1)
        users[len(users)] = self.name

        with open(usersFileName, 'w+') as outfile:
            json.dump(users, outfile)
        menu()

    def validateUser(self,userID):
        users = json.load(open(usersFileName, "r"))

        if userID in users:
            return False
        else:
            print "User does not exist. Insert a valid user"


def addUser():
    newUserName = raw_input("Insert new user name")
    newUser = user(newUserName)
    newUser.saveUser()
    menu()





def menu():
    option = raw_input("Ticket Manager: \n 1 - Open Ticket \n 2 - List Tickets \n 3 Create user")

    if option == "1":
        openTicket()
    elif option == "2":
        listTickets()
    elif option == "3":
        addUser()
    else:
        print("No valid option selected. Chose a valid option.")
        time.sleep(1)


menu()