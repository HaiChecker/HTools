#!/usr/bin/python
# -*- coding: UTF-8 -*-
class PortScan :
    def __init__(self,address,threadNumber,port):
        self.port = port
        self.address = address
        self.threadNumber = threadNumber

    def scan(self):
        print "test"
        