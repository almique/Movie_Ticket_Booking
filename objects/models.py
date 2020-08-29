from typing import Optional
from datetime import datetime
from typing import List, Optional
from objects.enumerations import Genre, TicketStatus, SlotType, CustomerTier
from fastapi import FastAPI, Path
from pydantic import BaseModel



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
    ticketSlot: datetime
    ticketStatus: TicketStatus


"""
class TicketSlot():
    def __init__(self, slotId: str, \
    slotDescription: str, \
    startTime: datetime, \
    endTime: datetime , \
    slotType: SlotType , \
    genre: Genre, \
    availTickets: int):
        self.slotId = slotId
        self.slotDescription = slotDescription
        self.startTime = startTime
        self.endTime = endTime
        self.slotType = slotType
        self.genre = genre
        self.availTickets = availTickets
    

"""
class TicketSlot(BaseModel):
    slotId: str
    slotDescription: str
    startTime: datetime
    endTime: datetime 
    slotType: SlotType 
    genre: Genre
    availTickets: int


class TicketCustomer(User):
    registrationDate: datetime
    customerTier : CustomerTier


class TicketAdmin(User):
    def __init__(self, isSystemAdmin=True):
        from objects.object_factories import TicketSlotFactory
        self.ticketSlotFactory = TicketSlotFactory()
        if(isSystemAdmin):
            self.userName = "system"
            self.userId = 0


    def bookCustomerTicket(self) -> Ticket:
        pass

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

    def scheduleTicketSlot(self, slotDescription: str, \
                            startTime: datetime, \
                            endTime: datetime, \
                            slotType: TicketSlot, \
                            genre: Genre) -> TicketSlot:
        
        return self.ticketSlotFactory.createTicketSlot(slotDescription, startTime, endTime, slotType, genre)
        

    def getAvailableTicketSlots(self) -> List[TicketSlot]:
        pass


    
