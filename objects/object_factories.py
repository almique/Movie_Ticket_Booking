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
            arguments: Details of a ticket slot
            return_type: TicketSlot Object
            description: Validates and saves a new TicketSlot
        """
        ticketSlot = TicketSlotORM(slotId = str(random.randint(1,1000000)), \
            slotDescription = slotDescription, \
            startTime = startTime, \
            endTime = endTime, \
            slotType = slotType.value, \
                genre = genre.value, availTickets = 20)
        ticketSlot.save()
        return TicketSlot.from_orm(ticketSlot)