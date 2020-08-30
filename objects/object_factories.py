import random
from datetime import datetime
from objects.enumerations import * 
from objects.models import *
from objects.orm_model import *

class TicketSlotFactory():
    def __init__(self):
        super().__init__()
    
    def createTicketSlot(self, slotName: str, slotDescription: str, \
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
            slotName = slotName ,\
            slotDescription = slotDescription, \
            startTime = startTime, \
            endTime = endTime, \
            slotType = slotType.value, \
                genre = genre.value, availTickets = 20)
        ticketSlot.save()
        return TicketSlot.from_orm(ticketSlot)


class TicketFactory():
    def __init__(self):
        super().__init__()
    
    def createTicket(self, userId: str ,ticketSlot: TicketSlot) -> Ticket:
        ticket = TicketORM(ticketId = "TKT" + str(random.randint(1,1000000)),\
                            userId = userId ,\
                            ticketSlotId = ticketSlot.slotId,\
                            ticketStatus = TicketStatus.Booked)
        ticket.save()
        return Ticket.from_orm(ticket)
