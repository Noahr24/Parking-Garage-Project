class parkingGarage():


    def __init__(self, tickets, spaces, current_ticket):
        self.tickets = tickets
        self.spaces = spaces
        self.current_ticket = current_ticket


#This is Hong's part
    def addTicket(self):
        temp = self.tickets.pop()
        space = self.spaces.pop()
        self.current_ticket[temp] = "not paid"
        print(f'Your ticket and spot number is {temp}. We will see you when you pay.')
        if self.tickets == []:
            print("Sorry, there are no more spots available.")

#This is Noah's part
    def payTicket(self):
        user_input = int(input("Input your ticket number? "))
        self.current_ticket[user_input] = "paid"
        print("Thank you for paying, you have 15 minutes to leave. ")


#This is Noah's part    
    def leaveGarage(self):
        input_ticket = int(input("What is your ticket number? "))
        if self.current_ticket[input_ticket] == "paid":
            print("Thank you, have a nice day")
            self.tickets.append(input_ticket)
            self.spaces.append(input_ticket)
            del self.current_ticket[input_ticket] 
        elif self.current_ticket[input_ticket] != "paid":
            print("You need to pay your ticket before you leave. Please go back and pay for the ticket")


#This was Nate's 
def run():
    garage = parkingGarage([1,2,3], [1,2,3], {})
    while True:
        response = input("Do you to park, pay, or leave? (type 'quit' to quit)")
        if response.lower() == 'park':
            garage.addTicket()
        elif response.lower() == 'pay':
            garage.payTicket()
        elif response.lower() == 'leave':
            garage.leaveGarage()
        elif response.lower() == 'quit':
            break
        else:
            print("Not a valid input, please retry")


run()