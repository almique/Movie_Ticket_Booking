from typing import Optional
from objects.models import *
from fastapi import FastAPI
from datetime import datetime
from typing import List, Optional

app = FastAPI()
ticketAdmin = TicketAdmin()

@app.get("/")
def read_root():
    return {"Hello": "Worl"}


#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Optional[str] = None):
#    return {"item_id": item_id, "q": q}


@app.post("/scheduleMovie")
def scheduleMovie(slotName: str, slotDescription: str, \
                            startTime: datetime, \
                            endTime: datetime, \
                            slotType: SlotType, \
                            genre: Genre):
    return ticketAdmin.scheduleTicketSlot(slotName, slotDescription, startTime, endTime, slotType, genre)



@app.post("/bookTicket")
def bookTicket(userName: str, userPhoneNumber: str, movieName: str, movieStartTime: datetime, numTickets: int):
    user = ticketAdmin.resolveOrCreateUser(userName, userPhoneNumber)
    return ticketAdmin.bookCustomerTicket(user.userId, movieName, movieStartTime, numTickets)

@app.post("/updateMovieSlotForTicket")
def updateMovieSlotForTicket(ticketId: str, newMovie: str, newStartTime: datetime):
    ticket = ticketAdmin.getTicketById(ticketId)
    ticketSlot = ticketAdmin.resolveTicketSlot(newMovie, newStartTime)[0]
    return ticketAdmin.updateTicket(ticket, ticketSlot)
     

@app.post("/getAllTicketsForMovieSlot")
def getAllTicketsForMovieSlot(movieName: str, movieStartTime: datetime):
    ticketSlots = ticketAdmin.resolveTicketSlot(movieName, movieStartTime)
    for ticketSlot in ticketSlots:
        return ticketAdmin.getBookedTickets(ticketSlot)
    return []
     
@app.post("/cancelTicket")
def cancelTicket(ticketId: str):
    ticket = ticketAdmin.getTicketById(ticketId)
    ticketSlot = ticketAdmin.getTicketSlotById(ticket.ticketSlotId)
    return ticketAdmin.cancelTicket(ticket, ticketSlot)
 
@app.post("/getUserDetailsByTicketId")
def getUserDetailsByTicketId(ticketId: str):
    ticket = ticketAdmin.getTicketById(ticketId)
    print(ticket, ticket.userId)
    user = ticketAdmin.getUserById(ticket.userId)
    return User.from_orm(user) 
 