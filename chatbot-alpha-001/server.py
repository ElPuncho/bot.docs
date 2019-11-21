#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket, pickle
import py_files.controller as cont

class Server:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.CONN = None
        self.ADDR = None
        self.DATA = None
        self.bufferSize = 1024
        self.SOCKET = None
        self.CONT = None
        
    def bindSocket(self):
        self.SOCKET.bind((self.HOST, self.PORT))
    
    def letSocketListen(self):
        self.SOCKET.listen()
    
    def getClientConnectInformation(self):
        self.CONN, self.ADDR = self.SOCKET.accept()
    
    def recieveClientData(self):
        self.DATA = self.CONN.recv(self.bufferSize)
        
    def sendClientDataToControlClass(self):
        self.CONT = cont.ControlManager(pickle.loads(self.DATA))
        self.CONT.initSession()
        self.CONT.crawlQuery()
        self.DATA = pickle.dumps(self.CONT.executeFiltering())
        self.CONT.closeSession()
    
    def sendDataToClient(self):
       self.CONN.sendall(self.DATA)
    
    def execute(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.SOCKET:
            self.bindSocket()
            self.letSocketListen()
            self.getClientConnectInformation()
            with self.CONN:
                print("Client:", self.ADDR)
                while True:
                    self.recieveClientData()
                    if not self.DATA:
                        break
                    self.sendClientDataToControlClass()
                    self.sendDataToClient()

if __name__ == "__main__":
    s = Server("127.0.0.1", 65432)
    s.execute()