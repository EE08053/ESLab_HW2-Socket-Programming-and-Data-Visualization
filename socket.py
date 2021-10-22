#!/usr/bin/env python3
import socket
import numpy as np
import json
import time
import random
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

HOST = '0.0.0.0'        # Standard loopback interface address 
PORT = 8000            # Port to listen on (use ports > 1023)

data_s = []
def store(dat, ds):
    # "{\"x\":%f,\"y\":%f,\"z\":%f,\"s\":%d}"
    a = dat.split(",")
    d = []
    for i in range(3):
        b = a[i].split(":")
        d.append(int(b[1]))
    ds.append(d)

print("start")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Connected by', addr)
        data_num = 0 
        target_num = 100
        while data_num < target_num:
            data = conn.recv(1024).decode('utf-8')
            store(data, data_s)
            print('Received from socket server : ', data)
            data_num += 1
# visualization
data_draw = np.array(data_s[1:])
t = np.arange(1,len(data_draw)+1)
plt.figure(figsize=(15,10),dpi=100,linewidth = 2)

plt.plot(t,data_draw[:,0],'o-',color = 'r', label="X")
plt.plot(t,data_draw[:,1],'o-',color = 'g', label="Y")
plt.plot(t,data_draw[:,2],'o-',color = 'b', label="Z")

plt.title("Accelero from STM-32", x=0.5, y=1.03)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("time(s)", fontsize=30, labelpad = 15)
plt.ylabel("value", fontsize=30, labelpad = 20)
plt.legend(loc = "best", fontsize=20)
plt.show()
print("finish")