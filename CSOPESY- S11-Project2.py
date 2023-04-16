import threading
from threading import *
from numpy.random import *
import time


class ThreadID:
    def __init__(self, id, color):
        self.id = id
        self.color = color
        
def dressingRoom(ThreadID):
    global maxSlot
    global customersLeft
    print(f'{ThreadID.color} {ThreadID.id} is attempting to enter the dressing room')
    maxSlot.acquire()
    customersLeft = customersLeft - 1
    print(f'{ThreadID.color} {ThreadID.id}  has entered the dressing room')
    maxSlot.release()
    print(f'{ThreadID.color} {ThreadID.id}  has left the dressing room')

    

def main():
    n = int(input('Enter the number of slots in the fitting room:'))
    b = int(input('Enter the number of blue threads:'))
    g = int(input('Enter the number of green threads:'))

    global maxSlot
    maxSlot = BoundedSemaphore(n)


    # [0] Blue First, [1] Green First
    chooser = randint(2)
    
    global curr_color
    
    if (chooser == 1 and g > 0) or (chooser == 0 and (b <= 0 and g > 0)):
        curr_color = 'Green'
    elif (chooser == 0 and b > 0) or (chooser == 1 and (b > 0 and g <= 0 )):
        curr_color = 'Blue'

    blueCounter = 1
    greenCounter = 1
    
    global customersLeft
    customersLeft = g + b
    
    while customersLeft > 0:
        i = 0
        if curr_color == 'Blue':
            while i < n and b > 0: 
                Thread(target=dressingRoom, args = [ThreadID(blueCounter, curr_color)]).start()
                i = i + 1
                b = b - 1
                blueCounter = blueCounter + 1
            curr_color = 'Green'
        else:
            while i < n and g > 0:
                Thread(target = dressingRoom, args = [ThreadID(greenCounter, curr_color)]).start()
                i = i + 1
                g = g - 1
                greenCounter = greenCounter + 1
            curr_color = 'Blue'
    

if __name__ == '__main__':
    main()