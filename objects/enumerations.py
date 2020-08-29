import enum

class Genre(enum.Enum):
    Action = 1
    Adventure = 2
    Comedy = 3
    Crime = 4
    Drama = 5
    Fantasy = 6
    Historical = 7
    Historical_Fiction = 8
    Horror = 9
    Magical_Realism = 10
    Mystery = 11
    Philosophical = 12
    Political = 13
    Romance = 14
    Saga = 15
    Satire = 16
    Scifi = 17
    Social = 18
    Speculative = 19
    Thriller = 20
    Urban = 21
    Animation = 22
    Documentary = 23
    Concert = 24

class TicketStatus(enum.Enum):
    Expired = 0
    Active = 1
    Archived = 2
