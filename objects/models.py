from typing import Optional
import datetime
from objects.enumerations import Genre, TicketStatus
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    """
        Defines a base abstract class for user
    """
    userId: str
    userName: str
    __phoneNumber: str
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

class TicketSlot(BaseModel):
    slotId: str
    slotDescription: str
    startTime: datetime 
    endTime: datetime 
    slotType: TicketSlot 
    genre: Genre
    availTickets: int

class TicketAdmin(User):
    def bookCustomerTicket(self) -> Ticket:
        pass

    def updateCustomerTicket(self) -> Ticket:
        pass

    def getBookedTickets(self, ticketSlot) -> List[Ticket]:
        pass

    def deleteTicket(self, ticket) -> Boolean:
        pass

    def getCustomerDetail(self, ticket) -> TicketCustomer :
        pass

    def invalidateTickets(self) -> List[Ticket]:
        pass

    def scheduleTicketSlot(self) -> TicketSlot:
        pass

    def getAvailableTicketSlots(self) -> List[TicketSlot]:
        pass


    
