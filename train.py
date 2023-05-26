import time
from observer import observer
import threading

def train():
    while not observer.stop_training: 
        time.sleep(3)
        print("Training..")
        

def start_train():
    train_thread = threading.Thread(target=train)
    train_thread.start()
    