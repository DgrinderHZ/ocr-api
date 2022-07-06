from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

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
