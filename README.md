# fast-api
- [스터디 내용 정리 노션 페이지](https://www.notion.so/Fast-API-b30c9f8cde114faab84beffccab0ca19)

<br>


## FastAPI basic Settings
- virtual environment setting : `python -m venv myvenv`
- fastapi installation : `pip install fastapi`
- uvicorn installation : `pip install uvicorn` (a high performance ASGI Server)
- hypercorn installation : `pip install hypercorn` (an ASGI server compatible with HTTP/2and Trio among other features)
<br>


- localhost runserver : `uvicorn main:app --reload`

<br>

### Extra Installation

- database installation : `pip install databases`
- pydantic installation : `pip install pydantic` (For data validation and settings management - python type annotation)
- pymysql installation : `pip install --upgrade pymysql`
- Starlette installation : `pip install starlette` (a lightweight ASGI framework- building async web services in PYthon - WebSocket support, test client built on requests, session and cookie support, CORS, GZip, Static Files, Streaming Responses)
- Jinja2 Templates installation : `pip install jinja2` 

<br>

- localhost runserver : `uvicorn main:app --reload`

<br>

## fastAPI CRUD

## web CRUD