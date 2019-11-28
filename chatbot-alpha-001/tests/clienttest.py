#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import client.client as cl

class TestClient(unittest.TestCase):
    def testInit(self):
        c = cl.Client("127.0.0.1", 65432)
        self.assertEqual(c.PORT, 65432)
        self.assertEqual(c.HOST, "127.0.0.1")
        self.assertEqual(c.bufferSize, 1024)
        self.assertEqual(c.SOCKET, None)
        

if __name__ == "__main__":
    unittest.main()
