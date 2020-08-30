from typing import Optional
from datetime import datetime
from typing import List, Optional
from objects.enumerations import Genre, TicketStatus, SlotType, CustomerTier
from fastapi import FastAPI, Path
from pydantic import BaseModel
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from objects.orm_model import *
#from controllers.ticketController import *

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
    





    
 