from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute
)
import os

class UserORM(Model):
    class Meta:
        table_name = "ticketslots"
        region = os.environ['AWS_DEFAULT_REGION']
    userId =  UnicodeAttribute(null=False, hash_key=True)
    userName =  UnicodeAttribute(null=False)
    __phoneNumber = UnicodeAttribute(null=False)

class TicketSlotORM(Model):
    """
    A DynamoDB TickeSlot 
    """
    class Meta:
        table_name = "ticketslots"
        region = os.environ['AWS_DEFAULT_REGION']
    slotId = UnicodeAttribute(null=False, hash_key = True)
    slotName = UnicodeAttribute(null=False)
    slotDescription = UnicodeAttribute(null=True)
    startTime =  UTCDateTimeAttribute()
    endTime = UTCDateTimeAttribute()
    slotType =  UnicodeAttribute(null=False) 
    genre = UnicodeAttribute(null=False)
    availTickets = NumberAttribute(default=20)

    def __repr__(self):
        return "Movie({}, {}, {})".format(self.slotId, self.slotName, self.startTime)

class TicketORM(Model):
    class Meta:
        table_name = "tickets"
        region = os.environ['AWS_DEFAULT_REGION']
    ticketId = UnicodeAttribute(null=False, hash_key=True)
    userId = UnicodeAttribute(null=False)
    ticketSlotId = UnicodeAttribute(null = False)
    ticketStatus =UnicodeAttribute(null=False, default = "Booked")

    