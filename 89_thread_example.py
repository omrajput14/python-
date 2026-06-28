# Multi-threading Example
import threading
import time

def print_numbers():
    for i in range(1, 6):
        time.sleep(0.1)
        print(f"Number {i}")

def print_letters():
    for letter in 'abcde':
        time.sleep(0.1)
        print(f"Letter {letter}")

if __name__ == "__main__":
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    print("Threads finished executing.")
