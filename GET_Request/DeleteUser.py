import requests
import json
import jsonpath


"""API Url"""
url = "https://reqres.in/api/users/2"


"""response for Deleting  a request"""
response =  requests.delete(url)

"""Fetching response code"""
print(response.status_code)


"""validating delete response """
assert response.status_code == 204