#! python3
# -*- coding: UTF-8 -*-

import socket               # 导入 socket 模块
import struct
 
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
client.connect(('localhost', 8888)) #建立一个链接，连接到本地的6969端口        # 设置端口号
 
instruction_id = '2020040901     '
investor_id = '161463          '
strategy_id = '001       '
instrucment_id = 'a2005 '
direction = 'b'
open_close_flag = '0'
limit_flag = '0'

volume = struct.pack('>i', 1)
price = struct.pack('>d', 4783)

msg = instruction_id + investor_id + strategy_id + \
	instrucment_id + direction + open_close_flag + limit_flag  #strip默认取出字符串的头尾空格
client.send(msg.encode('ascii'))  #发送一条信息 python3 只接收btye流
client.send(volume)
client.send(price)

data = client.recv(1024) #接收一个信息，并指定接收的大小 为1024字节
print('recv:',data.decode()) #输出我接收的信息
client.close()