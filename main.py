from fastapi import FastAPI

from typing import Optional
from pydantic import BaseModel, EmailStr, Field

import requests

# 앱 생성
app = FastAPI()

# db 리스트 생성
db = []

# User 모델
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr

class UserOut(BaseModel):
    username: str
    email: EmailStr

@app.post("/user/", response_model=UserOut)
async def create_user(user:UserIn):
    return user    

# 게시글 Board 모델
class Board(BaseModel):
    title: str          # 멘토링 팀 공고 제목
    author: str         # 게시글 작성자
    contents: Optional[str] = Field(None, title="멘토링 모집글 내용을 작성해주세요.")       # 게시물 내용
    target: str         # 멘토링 대상

# City 모델
class City(BaseModel):
    name: str
    timezone: str

# 루트 
@app.get("/")
async def root():
    return {"message": "Hello World"}


# City 전체 데이터 get
@app.get('/cities')
def get_cities():
    results = []
    for city in db:
        str = f"http://worldtimeapi.org/api/timezone/{city['timezone']}" # timezone 데이터를 문자열 형태로 가져옴
        print(str)
        r = requests.get(str)
        cur_time = r.json()['datetime']
        results.append({'name':city['name'], 'timezone':city['timezone'], 'current_time': cur_time}) # 새 객체 추가

    return results


# id에 따른 City 조회
@app.get('/cities/{city_id}')
def get_city(city_id: int):
    city = db[city_id-1]
    r = requests.get(f"http://worldtimeapi.org/api/timezone/{city['timezone']}")
    cur_time = r.json()['datetime']
    return {'name':city['name'], 'timezone':city['timezone'], 'current_time': cur_time}


# city 데이터 생성
@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())
    return db[-1]


# city 데이터 삭제
@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)
    return {}