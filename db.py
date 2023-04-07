import pymongo
import json

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

## creating the  named "kimo"
myDb = myClient["kimo"]

##creating the collection named "courses"
myCollection = myDb["courses"]

##parsing the json file
file = open('courses.json')

data = json.load(file)

#add the ratings field for each chapter of a course and adding total rating field for each course
for course in data:
    chapters = course["chapters"]
    for chapter in chapters:
        chapter.update({
            "rating": 0
        })
    course.update({
        "total rating": 0
    })

## to enter the data in the DB, commented after running once
#myCollection.drop()
#myCollection.insert_many(data)
