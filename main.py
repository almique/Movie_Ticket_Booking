from typing import Optional
from objects.models import *
from fastapi import FastAPI
from datetime import datetime
from typing import List, Optional

app = FastAPI()
ticketAdmin = TicketAdmin()

@app.get("/")
def read_root():
    return {"Hello": "Worl"}


#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Optional[str] = None):
#    return {"item_id": item_id, "q": q}


@app.post("/scheduleMovie")
def scheduleMovie(slotName: str, slotDescription: str, \
                            startTime: datetime, \
                            endTime: datetime, \
                            slotType: SlotType, \
                            genre: Genre):
    return ticketAdmin.scheduleTicketSlot(slotName, slotDescription, startTime, endTime, slotType, genre)



@app.post("/bookTicket")
def bookTicket(userName: str, userPhoneNumber: str, movieName: str, movieStartTime: datetime, numTickets: int):
    user = ticketAdmin.resolveOrCreateUser(userName, userPhoneNumber)
    return ticketAdmin.bookCustomerTicket(user.userId, movieName, movieStartTime, numTickets)
    

 