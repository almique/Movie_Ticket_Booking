import random
from datetime import datetime
from objects.enumerations import * 
from objects.models import TicketSlot
from objects.orm_model import *

class TicketSlotFactory():
    def __init__(self):
        super().__init__()
    
    def createTicketSlot(self, slotDescription: str, \
                            startTime: datetime, \
                            endTime: datetime, \
                            slotType: TicketSlot, \
                            genre: Genre) -> TicketSlot:
        """   
        return TicketSlot(slotId = str(random.randint(1,1000000)), \
            slotDescription = slotDescription, \
            startTime = startTime, \
            endTime = endTime, \
            slotType = slotType, \
                genre = genre, availTickets = 20) # add a class for availticket
        """
        ticketSlot = TicketSlotORM(slotId = str(random.randint(1,1000000)), \
            slotDescription = slotDescription, \
            startTime = startTime, \
            endTime = endTime, \
            slotType = str(slotType), \
                genre = str(genre), availTickets = 20)
        #ticketSlot.save()
        return TicketSlot.from_orm(slotId = str(random.randint(1,1000000)), \
            slotDescription = slotDescription, \
            startTime = startTime, \
            endTime = endTime, \
            slotType = slotType, \
                genre = genre, availTickets = 20)