#coding:utf-8
from urllib import request, parse 

url = "http://localhost/vSearch.GenericAPI/api/staffInfo"
# data = {}
# data["loginname"] = 'student08@qq.com'
# data["password"] = '96e79218965eb72c92a549dd5a330112'
# data = parse.urlencode(data)
# requesturl = url + '?' + data
requesturl = url
requestResponse = request.urlopen(requesturl)
ResonseStr = requestResponse.read()
ResonseStr = ResonseStr.decode('utf-8')
print(ResonseStr)