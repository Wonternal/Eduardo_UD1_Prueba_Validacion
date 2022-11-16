import os
from time import sleep
import datetime

def padre():
    
    newPid = os.fork()

    if (newPid == 0):
        hijo()

def hijo():
    now = datetime.datetime.now()
    print(f"Iniciando el proceso: {os.getpid()} a las <{now.hour}:{now.minute}:{now.second}>")
    sleep(3)
    print(f"Terminando el proceso con PID: {os.getpid()}")
    os._exit(0)

if __name__ == "__main__":
    for i in range(10):
        padre()
        sleep(10)
