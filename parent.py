import requests
from getinterests import parent_email

url = "https://us4.api.mailchimp.com/3.0/lists/4ae4822697/segments/48957/members"

payload = "{\n\t\"email_address\": \"kn_richardson@yahoo.com\"\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic U29mdHdhcmVTcXVhZDpjNTNmMzI1ZDM3OWZmYWQxNGM4MjdiMThlYThkM2NhMC11czQ=",
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "3b1e97f4-179a-4dba-ae7d-668aaa185108,40b3163c-c583-4933-8fa9-04780b6b9d86",
    'Host': "us4.api.mailchimp.com",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "47",
    'Cookie': "_mcid=1.f5607a9e4c637ec978c6a2c798a4bc50.8368069238ca9c2c441f1d4cb12d500ca74d9b48286ec0f95336f2a510b30186; _AVESTA_ENVIRONMENT=prod",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

#print(response.text)