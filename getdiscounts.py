import requests
from getinterests import dic

url = "https://fake-supermarket.myshopify.com/admin/api/2019-10/price_rules.json"

headers = {
    'Authorization': "Basic NjIwM2Y3YTUxYzYwODg0YzZiMGY0NDdhZDlmOTYxMjA6MmI4Nzg0ZDZjYTM1ZWQzY2NmYTdmODQ3NmI0NTYwNTU=",
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "1e12dd81-b029-4a21-8f91-945bce71af99,471553ff-0a03-426d-8d2e-4b98106fe917",
    'Host': "fake-supermarket.myshopify.com",
    'Accept-Encoding': "gzip, deflate",
    'Cookie': "_master_udr=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWsxTWpFd1pUTmxZaTFrWkRJM0xUUXdPV010WWpWaE55MWpOMkUzWVdGbVptUmtNakFHT2daRlJnPT0iLCJleHAiOiIyMDIxLTEwLTE0VDE3OjMyOjI4LjIyNVoiLCJwdXIiOiJjb29raWUuX21hc3Rlcl91ZHIifX0%3D--a3f74b47068033c8ba017b2af55da78d76280fc4; _secure_admin_session_id=308b2ab5524146417bad6bdd6c2bd012; __cfduid=d01cb5da015a62576794d5fc2289177971571070382; _orig_referrer=https%3A%2F%2F6203f7a51c60884c6b0f447ad9f96120%3A2b8784d6ca35ed3ccfa7f8476b456055%40fake-supermarket.myshopify.com%2Fadmin%2Fapi%2F2019-10%2Fprice_rules.json; _landing_page=%2Fadmin%2Fauth%2Flogin",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

data = response.json()

#tags/email campaigns
foodie = ['baking', 'cook', 'produce', 'garden', 'drinks']
parent =  ['baby', 'garden', 'school', 'snack']
student = ['meal', 'school', 'snack']
general = []


        
#parse through array of user interests imported from getinterests.py
for user_fname, interest_list in dic.items():
    
    #go through user interests
    for one_interest in interest_list:
        
        #print(user_fname)
        if dic[user_fname] == foodie:
            #add user to foodie campaign
            dic[user_fname].append('foodie tag')
            #print(dic[user_fname])
            #print(" is a foodie!!")
            break
            
        if dic[user_fname] == parent:
            #add user to foodie campaign
            dic[user_fname].append('parent tag')
            #print(dic[user_fname])
            #print(" is a parent!!")
            break
            
        if dic[user_fname] == student:
            #add user to foodie campaign
            dic[user_fname].append('student tag')
            #print(dic[user_fname])
            #print(" is a student!!")
            break
            

            
        
            
        
        
        
        
        
    
        
        
        
        

        
         
        
