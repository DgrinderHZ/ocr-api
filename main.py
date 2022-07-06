from fastapi import FastAPI

app = FastAPI()

course_items = [{"course_name": "Python"}, {"course_name": "NodeJS"}, {"course_name": "Machine Learning"}]

@app.get('/')
def main():
    return {'message': 'hi, fasty!'}

@app.get('/courses/{course_name}')
def read_course(course_name):
    return {'course_name': course_name}

@app.get('/courses/{course_id}')
def read_course(course_id: int):
    return {'course_id': course_id}

# QUERY PARAMS
@app.get('/courses/')
def read_courses(start: int, end: int):
    return course_items[start : start + end]