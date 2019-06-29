import json
import requests


# #字典转换成json格式
# dict1= {"Name":{"FirstName":"Tom","LastName":"Lee"}, "Age":4,"Category":"Cat"}, \
#        {"Name":{"FirstName":"Jerry","LastName":"Gray"}, "Age":3,"Category":"Mouse"}, \
#        {"Name":{"FirstName":"Mickey","LastName":"Joey"}, "Age":16,"Category":"CartoonMouse"}, \
#        {"Name":{"FirstName":"Donald","LastName":"Trump"}, "Age":18,"Category":"Duck"}
#
# obj = json.dumps(dict1) #老师的野路子：S是降为string类型
# print(obj)
# print(type(obj))
#
# myjob = json.loads(obj)
# print(myjob)
# print(type(myjob))
#
#
# #练习：将Donald和Trump的值取出来
# print(myjob[3]['Name']["LastName"])
#
# #练习：把所有的LastName都拿出来
#
# for t in myjob:
#     #print(t['Name']['LastName'])
#     print(t['Name']['FirstName'],t['Age'])


# dict2 = {
#     "Students":[
#         {"firstname":"John","lastname":"Doe"},
#         {"firstname":"Mary","lastname":"Tran"},
#         {"firstname":"Peter","lastname":"Jones"}
#     ]}
#
# obj1 = json.dumps(dict2)
# print(obj1)
# myjson1 = json.loads(obj1)
# print(myjson1)
# print(type(myjson1))
#
#
# for i in myjson1['Students']:
#     print(i['firstname'])


#基本工作当中拿到的是dumps后的结果，所以拿到之后要loads一下
# url = "https://suggest.taobao.com/sug?code=utf-8&q=%E4%BF%9D%E6%B8%A9%E6%9D%AF"
# # url = "https://api.weixin.qq.com/cgi-bin/user/info?access_token=ACCESS_TOKEN&openid=OPENID&lang=zh_CN"
# s = requests.get(url)
# print(s.text)
# print(json.loads(s.text))
json.dumps()
payload = {"key1":'value1',"key2":'value2',"key3":None}
r = requests.get("http://httpbin.org/get",params=payload)
print(r.json())
jsoncontent = r.json()
print(jsoncontent['headers']['Host'])



