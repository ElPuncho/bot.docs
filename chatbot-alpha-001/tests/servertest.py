#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import  server.server as sev

class TestServer(unittest.TestCase):
    def testInit(self):
        host, port = "127.0.0.1", 65432
        s = sev.Server(host, port)
        self.assertEqual(s.HOST, host)

if __name__ == "__main__":
    unittest.main()
        

