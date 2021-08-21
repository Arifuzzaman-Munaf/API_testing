import requests
import json
import jsonpath


"""API Url"""
url = "https://reqres.in/api/users?page=2"

"""sending GET request"""
response = requests.get(url)
# print(response)

"""Displaying response contents"""
print("Contents\n",response.content)

print("____________________________________________")

"""Displaying the header of Response"""
print("Header\n", response.headers)

print("____________________________________________")
"""Parse response to Json format"""
json_response = json.loads(response.text)

print("Json Format\n", json_response)

print("____________________________________________")

"""Fetch values using JsonPath"""
pages = jsonpath.jsonpath(json_response, 'total_pages')
print("total pages =", *pages)


"""testing whether it shows error or not"""
assert pages[0] == 2
