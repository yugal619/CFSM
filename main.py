import requests
import json

# url = 'http://52.22.123.139/api/register'
# body = {
#     "name":"testuser",
#     "email":"ayush.developerbox+3@gmail.com",
#     "password":"12345678",
#     "password_confirmation":"12345678"
# }


url = 'http://52.22.123.139/api/login'

body = {
    "email":"ayush.developerbox+2@gmail.com",
    "password":"12345678"
}

headers = {'Content-type': 'application/json',
           'X-Requested-With': 'XMLHttpRequest'
    }

x = requests.post(url, headers=headers, json=body)

print(x)
print(x.status_code)
print(x.headers['content-type'])
print(x.json())