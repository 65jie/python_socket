#! python3

import socket               # 导入 socket 模块
 
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口号
 
s.connect((host, port))
data = s.recv(1024) #接收一个信息，并指定接收的大小 为1024字节
print('recv:',data.decode()) #输出我接收的信息
s.close()