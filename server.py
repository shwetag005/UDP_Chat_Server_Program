# Importing Required Modules
import socket as s
import threading as thd
import time

# Create a Socket and Bind IP and PORT to It
skt = s.socket(s.AF_INET, s.SOCK_DGRAM)
localIP = input("Enter Your IP: ")
skt.bind((localIP, 8081))
print()

# Function to Recieve and Print the Message
def recv_msg():
    while True:
        msgRcv = skt.recvfrom(1024)
        print(msgRcv[1][0] + ": " + msgRcv[0].decode())
        time.sleep(10)

# Threads for Recieve Message Function
rcv_thd1 = thd.Thread(target=recv_msg)
rcv_thd2 = thd.Thread(target=recv_msg)
rcv_thd3 = thd.Thread(target=recv_msg)
rcv_thd4 = thd.Thread(target=recv_msg)
rcv_thd5 = thd.Thread(target=recv_msg)
rcv_thd6 = thd.Thread(target=recv_msg)
rcv_thd7 = thd.Thread(target=recv_msg)

# Starting Threads
rcv_thd1.start()
rcv_thd2.start()
rcv_thd3.start()
rcv_thd4.start()
rcv_thd5.start()
rcv_thd6.start()
rcv_thd7.start()