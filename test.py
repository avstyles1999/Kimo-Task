import requests
import json

host_url = "http://localhost:8000"

## test to check the functionality of the api to get the list of all the available courses
response_code = requests.get(host_url + "/1/artificial intelligence")
print("the response for this request is")
print(response_code)

response_result = (json.dumps(response_code.json(),indent=4))
print(response_result)

response_code = requests.get(host_url + "/2/NA")
print("the response for this request is")
print(response_code)

response_result = (json.dumps(response_code.json(),indent=4))
print(response_result)

## test to check the functionality of the api to get an overview of the specified course
response_code = requests.get(host_url + "/course/Introduction to Programming")
print("the response for this request is")
print(response_code)

response_result = (json.dumps(response_code.json(),indent=4))
print(response_result)

response_code = requests.get(host_url + "/course/Computer Vision Course")
print("the response for this request is")
print(response_code)

response_result = (json.dumps(response_code.json(),indent=4))
print(response_result)

## test to check the functionality of the api to get information of the specified chapter of the specified course
response_code = requests.get(host_url + "/course/Computer Vision Course/Introduction to Convolutional Neural Networks for Visual Recognition")
print("the response for this request is")
print(response_code)

response_result = (json.dumps(response_code.json(),indent=4))
print(response_result)

response_code = requests.get(host_url + "/course/Introduction to Programming/CS50 2021 in HDR - Lecture 6 - Python")
print("the response for this request is")
print(response_code)

response_result = (json.dumps(response_code.json(),indent=4))
print(response_result)

## test to check the functionality of the api to add rating to each chapter
response_code = requests.put(host_url + "/course/Introduction to Programming/CS50 2021 in HDR - Lecture 6 - Python/4")
print("the response for this request is")
print(response_code)

response_result = (json.dumps(response_code.json(),indent=4))
print(response_result)

response_code = requests.put(host_url + "/course/Computer Vision Course/Introduction to Convolutional Neural Networks for Visual Recognition/2")
print("the response for this request is")
print(response_code)

response_result = (json.dumps(response_code.json(),indent=4))
print(response_result)