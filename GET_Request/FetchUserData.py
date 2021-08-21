import requests


"""API Url"""
url = "https://reqres.in/api/users?page=2"

"""sending GET request"""
response = requests.get(url)
# print(response)

"""Displaying response contents"""
print("Contents\n",response.content)

print("____________________________________________")

"""Displaying the header of Response"""
print("Header\n",response.headers)
