from fastapi import FastAPI
import uvicorn
from starlette.responses import RedirectResponse
from db import myCollection

app = FastAPI()

#api to add rating to each chapter
@app.put("/course/{course_name}/{chapter_name}/{rating}")
async def add_chapter_rating(course_name,chapter_name,rating="0"):
    for course in myCollection.find():
        if course['name'] == course_name:
            for chapter in course['chapters']:
                if chapter['name'] == chapter_name:
                    chapter.update({'rating' : chapter['rating'] + int(rating)})
                    print(chapter)
                    course.update({'total rating': course['total rating'] + int(rating)}) 
                    print(course)
                    myCollection.update_one({'name': course['name']}, {"$set": {'chapters': course['chapters'], 'total rating': course['total rating']}})
                    return {
                        "Updated Data": f"Successfully added the rating for the chapter {chapter_name} for the course {course_name}"
                    }
            return {
                "Chapter Information": f"The chapter {chapter_name} not found for the course {course_name}"
            }
    return {
        "Course Overview": f"Course {course_name} not found"
    }

#api to get information of the specified chapter of the specified course
@app.get("/course/{course_name}/{chapter_name}")
async def get_chapter_description(course_name,chapter_name):
    for course in myCollection.find():
        if course['name'] == course_name:
            for chapter in course['chapters']:
                if chapter['name'] == chapter_name:
                    return {
                        "Course": course['name'],
                        "Chapter Name": chapter['name'],
                        "Chapter Information": chapter['text'],
                        "Rating": chapter['rating']
                    }
            return {
                "Chapter Information": f"The chapter {chapter_name} not found for the course {course_name}"
            }
    return {
        "Course Overview": f"Course {course_name} not found"
    }

#api to get an overview of the specified course
@app.get("/course/{name}")
async def get_course_description(name):
    for course in myCollection.find():
        if course['name'] == name:
            return {
                "Course Overview": course['description'],
                "Chapters": course["chapters"],
                "Total Rating": course["total rating"]
            }
    return {
        "Course Overview": f"Course {name} not found"
    }

# api to get the list of all the available courses
@app.get("/{mode}/{filterValue}")
async def get_available_course(mode="1",filterValue="NA"):
    course_list=[]
    field="name"
    order=1
    if mode == "2":
        field="date"
        order=-1
    elif mode == "3":
        field="total rating"
        order=-1
    print(field,order)
    for course in myCollection.find().sort(field,order):
        if filterValue=="NA" or filterValue in course['domain']:
            course_list.append({
            "name": course['name'],
            "date": course['date'],
            "description": course['description'],
            "domian": course['domain'],
            "chapters": course['chapters'],
            "total rating": course['total rating'],
        })

    return {
        "List of Available Courses": course_list
    }

## re-route to the list of all available courses when the default url is hit
@app.get("/")
async def reroute():
    return RedirectResponse(url="/1/NA")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)