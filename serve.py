from ast import Global
from msilib import sequence
import socket
from socketData import*
import pickle
from event import *
from threading import Thread
import threading
import time

sequence_num=0
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
HOST = ip_address
class Server():
    '''Thực hiện mở máy chủ cho client kết nối 
    Truyền dữ liệu game
    '''
    def __init__(self):
        self.HOST = HOST  # Standard loopback interface address (localhost)
        self.PORT = 1  # Port to listen on (non-privileged ports are > 1023)
        self.Datagame=SocketData(0,0)
        self.OnReceive = event()
        self.OnConnect=event()
    def AddSubscribersForLockBrokenEvent(self,objMethod):
        self.OnReceive += objMethod
    def AddSubscribersForConnectEvent(self,objMethod):
        self.OnConnect += objMethod        
    def RemoveSubscribersForLockBrokenEvent(self,objMethod):
        self.OnReceive -= objMethod

    def sendData(self,Data):
        Data= pickle.dumps(Data)
        self.conn.sendall(Data)
        print("Serve gởi đi")
    def Start(self,HOST,Datagame,PORT,OnReceive):
        # pass
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            self.conn, self.addr = s.accept()
            with self.conn:
                print(f"Connected by {self.addr}")
                self.OnConnect()
                self.sendData(Data=SocketData(2,5))
                while True:
                    data = self.conn.recv(1024)
                    Datagame= pickle.loads(data)
                    self.Datagame=Datagame
                    OnReceive()
    def stop(self):
        pass
    def startServer(self):
        try:
            self.t1 = threading.Thread(target=self.Start,args=(self.HOST,self.Datagame,self.PORT,self.OnReceive))
            self.t1.start()
        except:
	        print ("error")
    
    