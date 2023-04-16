import threading
from threading import *
from numpy.random import *
import time

class ThreadID:
    def __init__(self, id, color):
        self.id = id
        self.color = color

def dressingRoom(ThreadID, colorSem, otherSem):
    global max_capacity
    print(f'{ThreadID.color} {ThreadID.id} is attempting to enter the dressing room\n')
    colorSem.acquire()
    print(f'{ThreadID.color} {ThreadID.id} has entered the dressing room\n')
    time.sleep(0.1)  # simulate trying on clothes
    colorSem.release()
    print(f'{ThreadID.color} {ThreadID.id} has left the dressing room\n')
    if colorSem._value == max_capacity - otherSem._value:
        otherSem.release()

def main():
    n = int(input("Number of slots inside the fitting room: "))
    b = int(input("Number of blue threads: "))
    g = int(input("Number of green threads: "))
  
    global max_capacity
    max_capacity = n

    blueSem = Semaphore(n)
    greenSem = Semaphore(n)

    # [0] Blue First, [1] Green First
    chooser = randint(2)
    
    global curr_color
    
    if (chooser == 1 and g > 0) or (chooser == 0 and (b <= 0 and g > 0)):
        curr_color = 'Green'
    elif (chooser == 0 and b > 0) or (chooser == 1 and (b > 0 and g <= 0)):
        curr_color = 'Blue'

    blueCounter = 1
    greenCounter = 1
    
    global customersLeft
    customersLeft = g + b
    
    while customersLeft > 0:
        i = 0
        if curr_color == 'Blue':
            print("Blue only.")
            while i < n and b > 0:
                Thread(target=dressingRoom, args=[ThreadID(blueCounter, curr_color), blueSem, greenSem]).start()
                i = i + 1
                b = b - 1
                blueCounter = blueCounter + 1
                if i == n and b > 0:
                    i = i - 1
            curr_color = 'Green'
        else:
            print("Green only.")
            while i < n and g > 0:
                Thread(target=dressingRoom, args=[ThreadID(greenCounter, curr_color), greenSem, blueSem]).start()
                i = i + 1
                g = g - 1
                greenCounter = greenCounter + 1
                if i == n and g > 0:
                    i = i - 1
            curr_color = 'Blue'
        time.sleep(0.1)  # add a small delay to prevent busy waiting
    
    print('All customers have finished trying on clothes.')
    

if __name__ == '__main__':
    main()
