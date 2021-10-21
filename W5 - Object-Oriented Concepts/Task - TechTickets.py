
# Global
myTickets = []


# Classes
class User:
    username = ""
    role = ""

    def __init__(self, username, role):
        self.username = username
        self.role = role

    # TODO: I need a better way of allocating ticket numbers.
    def AddTicket(self):
        issue = input("Enter issue: ")
        myTickets.append([len(myTickets), issue])


class Support(User):
    def __init__(self, username):
        User.__init__(self, username, role="Support")

    def RemoveTicket(self):
        ticketNumber = int(input("Enter ticket number: "))

        for x in myTickets:
            if x[0] == ticketNumber:
                myTickets.remove(x)
                print("Ticket removed.")
                break


# Main Logic
myUser = User("Aaron", "Standard")
myUser.AddTicket()

mySupport = Support("Admin")
mySupport.AddTicket()
mySupport.RemoveTicket()

print(myTickets)

