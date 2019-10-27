import requests
from getinterests import student_email

url = "https://us4.api.mailchimp.com/3.0/lists/4ae4822697/segments/48961/members"

payload = "{\n\t\"email_address\": \"jonbaile@cisco.com\"\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic U29mdHdhcmVTcXVhZDpjNTNmMzI1ZDM3OWZmYWQxNGM4MjdiMThlYThkM2NhMC11czQ=",
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "5d907d9b-6b3b-4f2e-8ee9-42d8e1a2dfb7,0aec457c-be59-4fa4-9d05-ae8b5fd103af",
    'Host': "us4.api.mailchimp.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "42",
    'Cookie': "_mcid=1.f5607a9e4c637ec978c6a2c798a4bc50.8368069238ca9c2c441f1d4cb12d500ca74d9b48286ec0f95336f2a510b30186; _AVESTA_ENVIRONMENT=prod",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

#print(response.text)