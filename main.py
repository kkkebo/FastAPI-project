import uvicorn
from api import users, sections, courses
from fastapi import Query, FastAPI, Path
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title='Fast API studying',
    description='API for studying fastAPI framework',
    version='0.0.1',
    contact={
        'name': 'Andrei',
        'email': 'andrey.k@exmpl.com',
    },
    license_info={
        'name': 'MIT',
    }
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)