import requests
from getinterests import foodie_email

url = "https://us4.api.mailchimp.com/3.0/lists/4ae4822697/segments/48953/members"

payload = "{\n\t\"email_address\": \"rachejon@cisco.com\"\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic U29mdHdhcmVTcXVhZDpjNTNmMzI1ZDM3OWZmYWQxNGM4MjdiMThlYThkM2NhMC11czQ=",
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "af49095a-ae69-469f-8cb1-595e076c652b,018c25c9-97c7-432c-9c60-c4942e3752ee",
    'Host': "us4.api.mailchimp.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "42",
    'Cookie': "_mcid=1.f5607a9e4c637ec978c6a2c798a4bc50.8368069238ca9c2c441f1d4cb12d500ca74d9b48286ec0f95336f2a510b30186; _AVESTA_ENVIRONMENT=prod",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

#print(response.text)