import requests


def get_info():
    s = requests.Session()
    param = {"page": 2}
    response = s.request("GET", "https://reqres.in/api/users", params=param)
    content = response.json()
    for i in content["data"]:
        if i["id"] == 8:
            return i["email"]


res = get_info()
print(res)
