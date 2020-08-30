from typing import Optional
from datetime import datetime
from typing import List, Optional
from objects.enumerations import Genre, TicketStatus, SlotType, CustomerTier
from fastapi import FastAPI, Path
from pydantic import BaseModel
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from objects.orm_model import *


class User():
    """
        Defines a base abstract class for user
    """
    userId: str
    userName: str
    __phoneNumber: str = None
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

    def updateStatus(self):
        pass
    def updateSlot(self):
        pass
    def getDetails(self):
        pass

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

    def fillTicket(Ticket):
        pass
    def releaseTicket(Ticket):
        pass


class TicketCustomer(User):
    registrationDate: datetime
    customerTier : CustomerTier

    def getBookedTickets() -> List[Ticket]:
        pass
    def increaseLoyality():
        pass
    def decreaseLoyality():
        pass
    


class TicketAdmin(User):
    def __init__(self, isSystemAdmin=True):
        from objects.object_factories import TicketSlotFactory, TicketFactory
        self.ticketSlotFactory = TicketSlotFactory()
        self.ticketFactory = TicketFactory()
        if(isSystemAdmin):
            self.userName = "system"
            self.userId = 0

    def getTicketSlots(self, slotName: str, startTime: datetime):
        return TicketSlotORM.scan((TicketSlotORM.slotName == slotName) & (TicketSlotORM.startTime == startTime))

    def bookCustomerTicket(self, userId: str, movieName: str, \
                          slotStartTime: datetime, numTickets: int) -> Ticket:
        ticketSlots = self.getTicketSlots(movieName, slotStartTime)
        for ticketSlot in ticketSlots:
            if ticketSlot.availTickets >= numTickets:
                return self.ticketFactory.createTickets(userId, ticketSlot, numTickets)
        return False

    def updateCustomerTicket(self) -> Ticket:
        pass

    def getBookedTickets(self, ticketSlot) -> List[Ticket]:
        pass

    def deleteTicket(self, ticket) -> bool:
        pass

    def getCustomerDetail(self, ticket) -> TicketCustomer :
        pass

    def invalidateTickets(self) -> List[Ticket]:
        pass
    
    def scheduleTicketSlot(self, slotName: str,slotDescription: str, \
                            startTime: datetime, \
                            endTime: datetime, \
                            slotType: TicketSlot, \
                            genre: Genre) -> TicketSlot:
        
        return self.ticketSlotFactory.createTicketSlot(slotName,slotDescription, startTime, endTime, slotType, genre)


    def getAvailableTicketSlots(self) -> List[TicketSlot]:
        pass


    
 