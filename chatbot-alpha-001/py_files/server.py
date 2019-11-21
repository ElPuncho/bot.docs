#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

class Server:
    def __init__(self, host, port):
        self.HOST = host
        self.Port = port
        self.CONN = None
        self.ADDR = None
        self.DATA = None
        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def bindSocket(self):
        self.SOCKET.bind((self.HOST, self.Port))
    
    def letSocketListen(self):
        self.SOCKET.listen()
    
    def getClientConnectInformation(self):
        self.CONN, self.ADDR = self.SOCKET.accept()
    
    def recieveClientData(self):
        self.DATA = self.CONN.recv(1024)
    
    def sendDataToClient(self):
       self.CONN.sendall(self.DATA)
    
    def execute(self):
        with self.CONN:
            print("Client:", self.ADDR)
        while True:
            self.recieveClientData()
            if not self.DATA:
                break
            self.sendDataToClient()
