import socket
import sys
import pickle
import queue
import tkinter
import threading

Root = tkinter.Tk()
Root.mainloop()
q = queue.Queue()

def on_main_thread(func):
    q.put(func)

def check_queue():
    while True:
        try:
            task = q.get(block=False)
        except Empty:
            break
        else:
            Root.after_idle(task)
    Root.after(100, check_queue)

def printLul():
    print("Lul")

def BigFunction():
    while x < 1000:
        if x == 100:
            on_main_thread(printLul)

t = threading.Thread(target = BigFunction)

Root.after(100, check_queue)
