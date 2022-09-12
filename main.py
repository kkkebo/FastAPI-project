from typing import Optional, List

import uvicorn
from fastapi import Query, FastAPI, Path
from pydantic import BaseModel

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

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get('/users', response_model=List[User])
async def get_users():
    return users


@app.post('/users')
async def create_user(user: User):
    users.append(user)
    return 'Successs'


@app.get('/user/{id}')
async def get_user(
        id: int = Path(..., description='The ID of the user you want to retrieve', gt=2),
        q: str = Query(None, max_length=5)
):
    return {'user': users[id], 'query': q}


if __name__ == '__main__':
    # noinspection PyTypeChecker
    uvicorn.run(app)
