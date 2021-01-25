# Importing Required Modules
import socket as s
import threading as thd
import os

# Create a Socket and Bind IP and PORT to It
skt = s.socket(s.AF_INET, s.SOCK_DGRAM)
localIP = input("Enter Your IP: ")
skt.bind((localIP, 8081))

# Get Partner's IP to chat with
usrIP = input("Enter Your Partner IP: ")
print()

# Function to Recieve and Print the Message
def recv_msg():
    while True:
        msgRcv = skt.recvfrom(1024)
        if msgRcv[0].decode() == "quit":
            print("Partner is Offline!")
            os._exit(1)
        print(msgRcv[1][0] + ": " + msgRcv[0].decode())

# Function to Send the Message
def send_msg():
    while True:
        data = input().encode()
        msgSent = skt.sendto(data, (usrIP, 8081))
        if data.decode() == "quit":
            os._exit(1)

# Thread for Send Message Function
send_thd = thd.Thread(target=send_msg)

# Threads for Recieve Message Function
rcv_thd = thd.Thread(target=recv_msg)

# Starting Threads
send_thd.start()
rcv_thd.start()