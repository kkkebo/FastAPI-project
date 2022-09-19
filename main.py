from api import users, sections, courses
from fastapi import FastAPI

from database.db_setup import engine
from database.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

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