# coding=utf-8
__author__ = 'Pedro'
__name__ = 'mTickets'
import os, time, json

ticketsFileName = os.getcwd() + "\Tickets.log"

#checks if tickets file JSON if exists. if not, creates file
# This is done in the lazy way an it preety bad
#
# This should be  static and use static counter to add or remove
# remember when loading the file we should get the max id to set as the 
# starting counter value

# I don't want you to ever mix standalone methods and classes!!!
def cTicketsFile():
    #if file exists
    if os.path.exists(ticketsFileName):
        print "Loading Users file"
        time.sleep(1)
        #if file not empty, load file
        if os.path.getsize(ticketsFileName) > 0:
            file=open(ticketsFileName, 'r+')
            #load records file
            tickets=json.load(file)
            file.close()
            #if any record exists return records
            if len(tickets)>0:
                return tickets
            #if file is not empty yet no records exist, load sample record to users instance.
            else:
                tickets = [{"status": "Open", "ticketID": 0, "userID": "0", "description": "Sample Description", "title": "Sample Title"}]
        #if file is empty, load sample record to users instance
        else:
            tickets = [{"status": "Open", "ticketID": 0, "userID": "0", "description": "Sample Description", "title": "Sample Title"}]
    #if file does not exist create file and load sample record to users instance
    else:
        #create new file
        file = open(ticketsFileName,'w+')
        file.close()
        print "Users file empty or not found. Formatting new Users file..."
        time.sleep(1)
        #load sample ticket into memory to write on exit
        tickets = [{"status": "Open", "ticketID": 0, "userID": "0", "description": "Sample Description", "title": "Sample Title"}]
    return tickets

# TICKETS CLASS#######################################
class ticket:
    def __init__(self, userID, title, description):
        self.userID = userID
        self.title = title
        self.description = description

    #returns tickets file if exists. if not, creates file

    def addTicket(self, newID):
        print('Adding ticket {0}...'.format(newID))
        time.sleep(1)
        #adds new record. ID is JSON length (always 1 bigger by default)

        data = {"ticketID": newID,
                "userID": self.userID,
                "title": self.title,
                "description": self.description,
                "status": "Open"}
        return data


def changeTicketStatus(ticketID,tickets):
    tickets=tickets
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
    return True

