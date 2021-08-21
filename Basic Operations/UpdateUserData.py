import requests
import json
import jsonpath


"""API Url"""
url = "https://reqres.in/api/users/2"

"""Read Input from Json file"""
file = open('UpdateUser.json', 'r')
json_input = file.read()

"""Parse json input to Json format"""
json_request = json.loads(json_input)

print("printing the json file ==>", json_request)

print("____________________________________________")

"""make POST request to send data from JSON file"""
response = requests.post(url, json_request)
print("Contents ==>", response.content)

print("____________________________________________")

"""Fetching header from the response"""
print("header of the response", response.headers)

print("____________________________________________")

"""Getting values for specific header"""
print('Content-Type', response.headers.get('Content-Type'))

"""validating response code for POST method"""
assert response.status_code == 201


"""Parse response to JSON format"""
Json_response = json.loads(response.text)


print("____________________________________________")
"""Pick ID for json path"""
id = jsonpath.jsonpath(Json_response, 'id')
print(*id)
