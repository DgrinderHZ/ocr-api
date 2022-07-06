import asyncio
import time
from typing import Optional
from urllib import response
from fastapi import BackgroundTasks, FastAPI
from backgrounds import write_notification

from models import Course

app = FastAPI()

course_items = [{"course_name": "Python"}, {"course_name": "NodeJS"}, {"course_name": "Machine Learning"}]

@app.get('/')
def main():
    return {'message': 'hi, fasty!'}

@app.get('/courses/{course_name}')
def read_course(course_name):
    return {'course_name': course_name}

@app.get('/courses_/{course_id}')
def read_course(course_id: int, q: Optional[str] = None):
    if q is not None:
        return {"course_name": course_items[course_id], "q": q} 
    return {"course_name": course_items[course_id]}

# QUERY PARAMS
@app.get('/courses/')
def read_courses(start: int = 0, end: int = 10):
    return course_items[start : start + end]

@app.post('/create')
def create(course: Course):
    return course

@app.post("/send-notification/{email}")
def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}


@app.get('/concurrent')
async def conc():
    tasks = []
    start = time.time()
    for i in range(2):
        tasks.append(asyncio.create_task(func1()))
        tasks.append(asyncio.create_task(func2()))
    response = await asyncio.gather(*tasks)
    end = time.time()
    return {'response': response, 'time_taken': (end-start)}


async def func1():
    await asyncio.sleep(2)
    return "Func1() Completed"

async def func2():
    await asyncio.sleep(1)
    return "Func2() Completed"