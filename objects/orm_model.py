from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute
)
import os

class TicketSlotORM(Model):
    """
    A DynamoDB TickeSlot 
    """
    class Meta:
        table_name = "ticketslots"
        region = os.environ['AWS_DEFAULT_REGION']
    slotId = UnicodeAttribute(null=False)
    slotDescription = UnicodeAttribute(null=True)
    startTime =  UTCDateTimeAttribute()
    endTime = UTCDateTimeAttribute()
    slotType =  UnicodeAttribute(null=False) 
    genre = UnicodeAttribute(null=False)
    availTickets = NumberAttribute(default=20)
    