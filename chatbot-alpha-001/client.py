#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket, pickle

class Client:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.bufferSize = 1024
        self.SOCKET = None
    
    def connectToServer(self):
        self.SOCKET.connect((self.HOST, self.PORT))
    
    def sendDataToServer(self, data):
        self.SOCKET.sendall(pickle.dumps(data))
    
    def recieveDataFromServer(self):
        return pickle.loads(self.SOCKET.recv(self.bufferSize))
    
    def printRecievedData(self):
        print(self.recieveDataFromServer())
    
    def execute(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.SOCKET:
            self.connectToServer()
            self.sendDataToServer(data)
            self.printRecievedData()

if __name__ == "__main__":
    print("Input:")
    query = input()
    c = Client("127.0.0.1", 65432)
    c.execute(query)