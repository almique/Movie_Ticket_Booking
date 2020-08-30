from typing import Optional
from datetime import datetime
from typing import List, Optional
from objects.enumerations import Genre, TicketStatus, SlotType, CustomerTier
from fastapi import FastAPI, Path
from pydantic import BaseModel
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from objects.orm_model import *


class User(BaseModel):
    """
        Defines a base abstract class for user
    """
    userId: str
    userName: str
    phoneNumber: str = None

    class Config:
        orm_mode = True
    def getPhoneNumber(self):
        return self.__phoneNumber

    def isAdmin(self):
        return False

class Ticket(BaseModel):
    """
        Defines a base abstract class for Ticket
    """
    ticketId: str
    userId: str
    ticketSlotId: int
    ticketStatus: TicketStatus

    class Config:
        orm_mode=True


"""

"""

from pydantic.dataclasses import dataclass


class TicketSlot(BaseModel):
    slotId: str
    slotName: str
    slotDescription: str
    startTime: datetime
    endTime: datetime 
    slotType: SlotType 
    genre: Genre
    availTickets: int
    
    class Config:
        orm_mode=True



class TicketCustomer(User):
    registrationDate: datetime
    customerTier : CustomerTier

    def increaseLoyality():
        pass
    def decreaseLoyality():
        pass
    


class TicketAdmin():
    def __init__(self, isSystemAdmin=True):
        from objects.object_factories import TicketSlotFactory, TicketFactory, UserFactory
        self.ticketSlotFactory = TicketSlotFactory()
        self.ticketFactory = TicketFactory()
        self.userFactory = UserFactory()
        if(isSystemAdmin):
            self.userName = "system"
            self.userId = 0

    def resolveOrCreateUser(self, userName: str, userPhoneNumber: str):
        return self.userFactory.resolveOrCreateUser(userName, userPhoneNumber)

    def getTicketSlotById(self, ticketSlotId: str):
        return TicketSlotORM.get(ticketSlotId)

    def getTicketById(self, ticketId: str):
        return TicketORM.get(ticketId)

    def getUserById(self, userId: str):
        return UserORM.get(userId)

    def resolveTicketSlot(self, slotName: str, startTime: datetime):
        return list(TicketSlotORM.scan((TicketSlotORM.slotName == slotName) & (TicketSlotORM.startTime == startTime)))

    def bookCustomerTicket(self, userId: str, movieName: str, \
                          slotStartTime: datetime, numTickets: int) -> Ticket:
        ticketSlots = self.resolveTicketSlot(movieName, slotStartTime)
        for ticketSlot in ticketSlots:
            if ticketSlot.availTickets >= numTickets:
                return self.ticketFactory.createTickets(userId, ticketSlot, numTickets)
        return False

    def updateTicket(self, ticket, newTicketSlot):
        newTicket = self.bookCustomerTicket(ticket.userId, newTicketSlot.slotName, newTicketSlot.startTime, 1)
        if newTicket:
            oldTicket = self.cancelTicket(ticket, self.getTicketSlotById(ticket.ticketSlotId))
            return [newTicket, oldTicket]
        return False


    def getBookedTickets(self, ticketSlot) -> List[Ticket]:
        return list(TicketORM.scan((TicketORM.ticketSlotId == ticketSlot.slotId) & (TicketORM.ticketStatus == TicketStatus.Booked.value)))

    def cancelTicket(self, ticket, ticketSlot) -> bool:
        return self.ticketFactory.cancelTicket(ticket, ticketSlot)


    def invalidateTickets(self) -> List[Ticket]:
        pass
    
    def scheduleTicketSlot(self, slotName: str,slotDescription: str, \
                            startTime: datetime, \
                            endTime: datetime, \
                            slotType: TicketSlot, \
                            genre: Genre) -> TicketSlot:
        
        return self.ticketSlotFactory.createTicketSlot(slotName,slotDescription, startTime, endTime, slotType, genre)



    
 