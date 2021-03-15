import requests


def get_info():
    s = requests.Session()
    param = {"page": 2}
    response = s.request("GET", "https://reqres.in/api/users", params=param)
    content = response.json()
    for i in content["data"]:
        if i["id"] == 8:
            return i["email"]

def changeint(value):
    if isinstance(value, int):
        return value
    elif isinstance(value, float):
        return int(value)
    elif isinstance(value, bool):
        return int(value)
    elif isinstance(value, str):
        try:
            return int(value)
        except:
            return "输入的字符不能转换为int类型"
    elif isinstance(value, type(None)):
        return "输入的字符不能转换为int类型"
    else:
        return "输入的字符不能转换为int类型"

def check_8():
    sorlist=[4,3,1,5,6,7]
    resultlist=[]
    for i in range(len(sorlist)):
        for j in range(i+1,len(sorlist)):
            if sorlist[i]+sorlist[j]==8:
                resultlist.append((i,j))
            else:
                continue
    return resultlist

def check_max_price():
    pricelist=[4,3,7,5,6,1]
    while True:
        if pricelist.index(sorted(pricelist)[-1])>pricelist.index(sorted(pricelist)[0]):
            return sorted(pricelist)[-1]-sorted(pricelist)[0]
        else:
            pricelist.remove(sorted(pricelist)[-1])
            pricelist.remove(sorted(pricelist)[0])
            continue


if __name__=="__main__":
    res=check_max_price()
    print(res)
    # res=check_8()
    # print(res)
    # res=changeint(1)
    # print(res)
    # res=changeint(2.5)
    # print(res)
    # res=changeint(True)
    # print(res)
    # res=changeint("张三")
    # print(res)
    # res=changeint("10")
    # print(res)
    # res=changeint(None)
    # print(res)
    # res = get_info()
    # print(res)
