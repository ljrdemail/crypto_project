import requests
import json

def get_message():
   s = requests.Session()
   param={"page":2}
   response=s.request("GET","https://reqres.in/api/users",params=param)
   content=response.json()
   msg=content["data"]
   for i in msg:
      if i["id"]==8:
         print(i["email"])


get_message()