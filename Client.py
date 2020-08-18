#Importing
import socket
import os
from time import sleep
#Function Called To Receive A File From Server
def ReceiveFile() :
    os.chdir("/sdcard/Download")
    FileName=input("Enter Name Of File : ")
    File=open(FileName,"wb")
    FileData=sock.recv(10000)
    File.write(FileData)
#Connect To Server
sock=socket.socket()
print("-"*84)
print("")
Host=str(input("Enter Ip Server :"))
print("")
print("[  A  .  Y .  O.  U.  B   A.  M.  E.  R  ]")
print("")
Port=int(input("Enter Port Server : "))
print("")
print("-"*84)
sock.connect((Host,Port))
print("connected...")
sleep(5)
ReceiveFile()
print("Complet")