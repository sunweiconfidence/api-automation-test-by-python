
#coding:utf-8
import urllib.request
import urllib.parse
data = urllib.parse.urlencode({"StaffID": "4455","LogStaffID":"3322","Name":"Joke","Status":"1","Staffs":"test"})
# f = urllib.parse.urlencode(d)
data = data.encode('utf-8')
#data = data.encode('utf-8')
request = urllib.request.Request("http://localhost/vSearch.GenericAPI/api/postStaffInfo")
 # adding charset parameter to the Content-Type header.
request.add_header("Content-Type","application/json;charset=utf-8")
f = urllib.request.urlopen(request, data)
print(f.read().decode('utf-8'))