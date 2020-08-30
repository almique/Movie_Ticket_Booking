from typing import Optional
from objects.models import *
from controllers.ticketController import *
from fastapi import FastAPI
from datetime import datetime
from typing import List, Optional

app = FastAPI(
    title="Ticketly",
    description="A Movie Theatre Ticket booking System  "
)

ticketAdmin = TicketAdmin()


@app.post("/bookTicket",
summary = "Book Tickets",
description = "Book Tickets using a user's name ,phoneNumber, Timing, MovieName"
) 
def bookTicket(userName: str, userPhoneNumber: str, movieName: str, movieStartTime: datetime, numTickets: int):
    user = ticketAdmin.resolveOrCreateUser(userName, userPhoneNumber)
    return ticketAdmin.bookCustomerTicket(user.userId, movieName, movieStartTime, numTickets)

@app.post("/updateMovieSlotForTicket",
summary = "Update a Ticket Time",
description = "Update Ticket Time by ticketId, newMovie and newStartTime")
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
 


@app.post("/scheduleMovie")
def scheduleMovie(slotName: str, slotDescription: str, \
                            startTime: datetime, \
                            endTime: datetime, \
                            slotType: SlotType, \
                            genre: Genre):
    return ticketAdmin.scheduleTicketSlot(slotName, slotDescription, startTime, endTime, slotType, genre)

@app.post("/getAllMovieSlots")
def getAllMovieSlotsByGenre():
    return ticketAdmin.getAllTicketSlots()



@app.post("/getAllMovieSlotsByGenre")
def getAllMovieSlotsByGenre(genre: Genre):
    return ticketAdmin.getAllTicketSlotsByGenre(genre)


"""
#TODO: Desirable Non-Functional Requirement
@app.post("/getAllMovieSlotsAfterTime")
def getAllMovieSlotsAfterTime(inputTime: datetime):
    return ticketAdmin.getAllMovieSlotsAfterTime(inputTime)

@app.post("/getAllMovieSlotsBeforeTime")
def getAllMovieSlotsBeforeTime(inputTime: datetime):
    return ticketAdmin.getAllMovieSlotsAfterTime(inputTime)
"""