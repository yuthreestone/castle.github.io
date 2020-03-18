from urllib import request
file = request.urlopen('http://cn.chinadaily.com.cn/')
message = file.read()
b = message.decode('utf-8')
print(b)
