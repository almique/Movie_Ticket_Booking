import random
from datetime import datetime
from objects.enumerations import * 
from objects.models import TicketSlot


class TicketSlotFactory():
    def __init__(self):
        super().__init__()
    
    def createTicketSlot(self, slotDescription: str, \
                            startTime: datetime, \
                            endTime: datetime, \
                            slotType: TicketSlot, \
                            genre: Genre) -> TicketSlot:
        return TicketSlot(str(random.randint(1,1000000)), slotDescription, startTime, endTime, slotType, genre, 20) # add a class for availticket