import dataclasses
from dataclasses import dataclass
from datetime import datetime

@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone_number: str
    date: datetime
    subject: str
    picture: str
    user_address: str
    user_state: str
    user_city: str
    gender:str
    hobbies: str
