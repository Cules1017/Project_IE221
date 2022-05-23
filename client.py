# echo-client.py
from socketData import*
import socket
import pickle
import time
from threading import Thread
import threading
from event import *
Data1=SocketData(3,0)
Data1= pickle.dumps(Data1)
class Client():
    '''Thực hiện kết nối với server
    Truyền dữ liệu game
        self.HOST = host của máy chủ
        self.PORT = port máy chủ mở
        self.Datagame=thông tin của game truyền đi
        self.OnReceive = sự kiên nhận được
        self.OnConnect= sự kiện khi kết nối
    '''
    def __init__(self,HOST,PORT):
        self.HOST = HOST  # The server's hostname or IP address
        self.PORT = PORT
        self.Datagame=SocketData(0,0)
        self.OnReceive = event()
        self.OnConnect=event()
    def AddSubscribersForLockBrokenEvent(self,objMethod):
        '''
        Thêm sự kiện khi nhận dữ liệu
        '''
        self.OnReceive += objMethod
    def AddSubscribersForConnectEvent(self,objMethod):
        '''
        Thêm sự kiện khi kết nối thành công
        '''
        self.OnConnect += objMethod
            
    def RemoveSubscribersForLockBrokenEvent(self,objMethod):
        """
        Gỡ sự kiện
        """
        self.OnReceive -= objMethod
    def sendData(self,Data):
        """
        Send data to server
        """
        Data= pickle.dumps(Data)
        self.s.sendall(Data)
        print("Client Gởi Di")
    def Connect(self,HOST,Datagame,PORT):
        '''
        Kết nối tới server
        '''
        print(self.HOST)
        print(self.PORT)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
            self.s.connect((HOST, PORT))
            self.OnConnect()
            while True:
                data = self.s.recv(1024)
                Datagame= pickle.loads(data)
                self.Datagame=Datagame
                self.OnReceive()
    def ConnectToServer(self):
        """
        Mở thêm một luồng truyền dữ liệu
        """
        try:
            t1 = threading.Thread(target=self.Connect,args=(self.HOST,self.Datagame,self.PORT))
            t1.start()
        except:
	        print ("error")
    