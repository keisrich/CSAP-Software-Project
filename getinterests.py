import requests

url = "https://us4.api.mailchimp.com/3.0/lists/4ae4822697/members"

payload = ""
headers = {
    'Authorization': "Basic U29mdHdhcmVTcXVhZDpjNTNmMzI1ZDM3OWZmYWQxNGM4MjdiMThlYThkM2NhMC11czQ=",
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "e0a0603e-827a-40e6-89f8-c60bc1c7c4ab,c0f132b4-62b1-45bb-a8b7-809155c83b8a",
    'Host': "us4.api.mailchimp.com",
    'Accept-Encoding': "gzip, deflate",
    'Cookie': "_mcid=1.f5607a9e4c637ec978c6a2c798a4bc50.8368069238ca9c2c441f1d4cb12d500ca74d9b48286ec0f95336f2a510b30186; _AVESTA_ENVIRONMENT=prod",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers)

data = response.json()

current_user = "null"
dic = {}
user_email = []


##parse through all members and return all true interests
for item in data['members']:  
    
   
    current_user = item['merge_fields']['FNAME']
    dic[current_user] = []
    #print(item['email_address'])
    user_email.append(item['email_address'])
    
    
    ##checks all interests to be true    
    if (item['interests']['ef40a668ea']):
        dic[current_user].append("baby")
        
    if (item['interests']['679b068e36']):
        dic[current_user].append("baking")
        
    if (item['interests']['0870482c97']):
        dic[current_user].append("cook")
    
    if (item['interests']['05a05383d0']):
        dic[current_user].append("produce")
        
    if (item['interests']['be6e13894b']):
        dic[current_user].append("garden")
        
    if (item['interests']['2dc4513102']):
        dic[current_user].append("gril")
        
    if (item['interests']['9f540ea5ad']):
        dic[current_user].append("health")
        
    if (item['interests']['c05c87578e']):
        dic[current_user].append("meal")
        
    if (item['interests']['dc3b892250']):
        dic[current_user].append("pets")
        
    if (item['interests']['c7eb0a3091']):
        dic[current_user].append("school")

    if (item['interests']['2661da2f4f']):
        dic[current_user].append("snack")
        
    if (item['interests']['d67f39cf24']):
        dic[current_user].append("drinks")  
            
        
#tags/email campaigns
foodie = ['baking', 'cook', 'produce', 'garden', 'drinks']
parent =  ['baby', 'garden', 'school', 'snack']
student = ['meal', 'school', 'snack']

#array of email addresses
foodie_email = []
student_email = []
parent_email = []


#compares user interests to tags 
#creates array of email addresses with a tag

for item in data['members']:  
       
    current_user = item['merge_fields']['FNAME']
    
    if dic[current_user] == foodie:
        foodie_email.append(item['email_address'])
        #print(foodie_email[0])
        #print("issa foodie")  
    if dic[current_user] == parent:
        parent_email.append(item['email_address'])
        #print(parent_email[0])
        #print("issa parent")
            
    if dic[current_user] == student:
        student_email.append(item['email_address'])
        #print(student_email[0])
        #print("issa student")

    