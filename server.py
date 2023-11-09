import socket
from _thread import *
import sys


server="192.168.0.107"#this is the IPV4 address of the machine that is running the server
port=5555#this is the port number only use port numbers that are not used

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen(2)#opens up the port so we can have multiple connections ect the number is number of clients
print ("waiting for connection, server started...")

def threaded_client(conn):
    
    reply=""
    
    while True:
        try:
            data=conn.recieve(2048)#2048 is the amount of information we want to recieve. you can increase this size. note the larger the size the longer itll take to recieve information.
            reply=data.decode("utf-8")#encoded information needs to be decoded into the format "utf-8"

            if not data:
                print("Disconnected")
                break
            else:
                print("Recieved: ",reply)
                print("sending: ",reply)
            
            conn.sendall(str.encode(reply))
        except:
            break
    print("lost connection")
    conn.close()

while True:
    conn,addr=s.accept()#store address and what is connected if something is found
    print ("connected to:",addr)

    start_new_thread(threaded_client,(conn,))

    #threading is like creating sub computers which run programs iin the background, we do not need to wait for the execution of those programs to continue 


