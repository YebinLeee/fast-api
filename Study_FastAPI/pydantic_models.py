
''' Pydantic Models '''

from datetime import datetime
from typing import List, Optional 

from pydantic import BaseModel 

class User(BaseModel):
    id: int
    name = "Yebin Lee"
    signup_ts : Optional[datetime]=None
    friends: List[int]=[]
    
external_data = {
    "id":"123",
    "signup_ts":"2017-06-01 12:22",
    "friends":[1, "2", b"3"], # int형만 인식
}

user = User(**external_data) # external_data 객체의 전체 데이터 전달
print(user)
print(user.id)