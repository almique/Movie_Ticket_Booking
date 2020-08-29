from enum import Enum

class Genre(str, Enum):
    Action = "Action"
    Adventure = "Adventure"
    Comedy = "Comedy"
    Crime = "Crime"
    Drama = "Drama"
    Fantasy = "Fantasy"
    Historical = "Historical"
    Historical_Fiction = "Historical Fiction"
    Horror = "Horror"
    Magical_Realism = "Magical Realism"
    Mystery = "Mystery"
    Philosophical = "Philosophical"
    Political = "Political"
    Romance = "Romance"
    Saga = "Saga"
    Satire = "Satire"
    Scifi = "Scifi"
    Social = "Social"
    Speculative = "Speculative"
    Thriller = "Thriller"
    Urban = "Urban"
    Animation = "Animation"

class TicketStatus(str, Enum):
    Expired = "Expired"
    Active = "Active"
    Archived = "Archived"

class SlotType(str, Enum):
    Movie = "Movie"
    Documentary = "Documentary"
    Concert = "Concert"

class CustomerTier(str, Enum):
    Gold = "Gold"
    Silver = "Silver"
    Platinum = "Platinum"
