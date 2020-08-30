from fastapi import FastAPI
from fastapi.testclient import TestClient
from typing import Optional
from fastapi import FastAPI
from datetime import datetime
from typing import List, Optional
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_bookTicket():
    response = client.post("/bookTicket",
        json={"userName": "kevin", "userPhoneNumber": "14567", "movieName": "The Foo Barters","movieStartTime":"2017-06-01 12:22","numTickets": "1" },
    )
    assert response.status_code == 422

def test_create_updateMovieSlotForTicket():
    response = client.post("/updateMovieSlotForTicket",
            json = {"ticketId": "17839", "newMovie": "Avatar", "newStartTime": "2017-06-01 12:22"}
    )
    assert response.status_code == 422

def test_create_getAllTicketsForMovieSlot():
    response = client.post("/getAllTicketsForMovieSlot",
            json = {"movieName": "17839", "movieStartTime": "2017-06-01 12:22"}
    )
    assert response.status_code == 422

def test_create_cancelTicket():
    response = client.post("/cancelTicket",
            json = {"ticketId": "1744339"}
    )
    assert response.status_code == 422

def test_create_getUserDetailsByTicketId():
    response = client.post("/getUserDetailsByTicketId",
            json = {"ticketId": "17439"}
    )
    assert response.status_code == 422

def test_create_scheduleMovie():
    response = client.post("/scheduleMovie",
            json = {"slotName": "Avatar", "slotDescription": "must watch",
             "startTime": "2017-06-01 12:22","endTime": "2017-06-01 12:22", "slotType": "Concert", "genre": "Action"}
    )
    assert response.status_code == 422

def test_create_getAllMovieSlotsByGenre():
    response = client.post("/getAllMovieSlotsByGenre",
            json = {"genre": ""}
    )
    assert response.status_code == 422
