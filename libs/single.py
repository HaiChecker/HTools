#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Queue

from threading import Thread
import sys
reload(sys)
import socket


class ScanPortThread(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            try:
                task = self.queue.get()
            except Queue.Empty:
                self.queue = True
                break
            TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            TCP_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            TCP_sock.settimeout(long(task[2]))
            try:
                success = TCP_sock.connect_ex(task[0], int(task[1])) == 0
            except:
                return False
            if success:
                self.queue.task_done()
            else:
                print ''
