
#coding:utf-8
import urllib.request
import urllib.parse
data = urllib.parse.urlencode({"StaffID": "4455","LogStaffID":"3322","Name":"Joke","Status":"1","Staffs":"test"})
# f = urllib.parse.urlencode(d)
data = data.encode('utf-8')
#data = data.encode('utf-8')
url = "http://localhost/vSearch.GenericAPI/api/newStaffInfo"
urlPara = {}

#urlPara["es"] = "elastic"
#urlPara["pageNo"] = 1
#urlPara = urllib.parse.urlencode(urlPara)
#requesturl = url + '?' + urlPara
requesturl = url + '/' + 'elastic'+'/'+ '1'
request = urllib.request.Request(requesturl)
 # adding charset parameter to the Content-Type header.
request.add_header("Content-Type","application/json;charset=utf-8")
f = urllib.request.urlopen(request, data)
print(f.read().decode('utf-8'))