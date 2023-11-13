print("running server.py...")

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


def read_pos(str):
    str=str.split(",")
    return int(str[0]),int(str[1])

def make_pos(tup):
    return str(tup[0])+","+str(tup[1])


pos=[(0,0),(100,100)]

def threaded_client(conn,player):

    conn.send(str.encode(make_pos(pos[player])))
    
    reply=""
    
    while True:
        try:
            data=read_pos(conn.recv(2048).decode()) #2048 is the amount of information we want to recieve. you can increase this size. note the larger the size the longer itll take to recieve information.
            pos[player]=data

            

            if not data:
                print("Disconnected")
                break
            else:
                if player==1:
                    reply=pos[0]
                else:
                    reply=pos[1]
                print("Recieved: ",reply)
                print("sending: ",reply)
            
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break
    print("lost connection")
    conn.close()

currentPlayer=0

while True:
    conn,addr=s.accept()#store address and what is connected if something is found
    print ("connected to:",addr)

    start_new_thread(threaded_client,(conn,currentPlayer))

    #threading is like creating sub computers which run programs iin the background, we do not need to wait for the execution of those programs to continue 
    currentPlayer=1

