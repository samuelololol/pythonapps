#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:  samuelololol
# Email:   samuelololol at google mail dot company
# Website: https://github.com/samuelololol/pythonapps/tree/master/thread
import threading
import Queue

thread_numbers = 4

class mythread(threading.Thread):
    def run(self):
        global Pool
        tname = threading.currentThread().getName()
        while True:
            item = Pool.get()
            if item != None:
                if item == 0:
                    break
                work(item,tname)
            Pool.task_done()
        Pool.task_done()

def work(item,name):
    global mutex
    mutex.acquire()
    print item,name
    mutex.release()

def main():
    global Pool, mutex, thread_numbers
    mutex = threading.Lock() 
    threads = []
    Pool = Queue.Queue(0)

    # example data
    ha = [1,2,3,4,5,6,7,8,9]

    # create threads
    for x in range(thread_numbers):
        threads.append(mythread())

    # all threads start
    for t in threads:
        t.start()

    # push item in to FIFO queue: Pool
    for item in ha:
        Pool.put(item)

    # add the leave condition for each thread
    for idx in range(thread_numbers):
        Pool.put(0)

    Pool.join()

if __name__ == '__main__':
    main()
