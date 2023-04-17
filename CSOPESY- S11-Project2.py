import threading
from threading import *
from numpy.random import *
import time


class ThreadID:
    def __init__(self, id, color):
        self.id = id
        self.color = color
        
def dressingRoom(ThreadID, limit, curr_color,b,g):
    global maxSlot
    global customersLeft
    global customersInside
    global blueThreads, greenThreads
    
    
    maxSlot.acquire()
    
    customersLeft = customersLeft - 1

    if curr_color == 'Green':
        greenThreads.append(ThreadID)
    else:
        blueThreads.append(ThreadID)

    print(f'{ThreadID.color} {ThreadID.id}  has entered the dressing room')
    
    if(customersInside == 0):
        print(f'{curr_color} only')

    customersInside = customersInside + 1

    if ((customersInside == limit)):
            if curr_color == 'Blue':
                while(len(blueThreads) > 0):
                    print(f'{blueThreads[0].color} {blueThreads[0].id} has left the dressing room')
                    blueThreads.pop(0)
                if b > 0:
                    print('Dressing Room Empty...')
                maxSlot.release(customersInside)

            else:
                while(len(greenThreads) > 0):
                    print(f'{greenThreads[0].color} {greenThreads[0].id} has left the dressing room')
                    greenThreads.pop(0)
                if g > 0:
                    print('Dressing Room Empty...')
                maxSlot.release(customersInside)
                                
            customersInside = 0
        


    

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
    
    global customersInside
    customersInside = 0
    
    global blueThreads, greenThreads
    blueThreads = []
    greenThreads = []
    
    handleBlueThreadsList = []
    handleGreenThreadsList = []


    while customersLeft > 0:
        i = 0
        if curr_color == 'Blue':
            while i < n and b > 0: 
                blueThread = ThreadID(blueCounter, curr_color)
                
                thread = Thread(target=dressingRoom, args = [blueThread, n, curr_color,b,g])
                thread.start()
                
                handleBlueThreadsList.append(thread)
                
                i = i + 1
                b = b - 1
                blueCounter = blueCounter + 1
            
            for t in handleBlueThreadsList:
                t.join()
            
            curr_color = 'Green'

        else:
            while i < n and g > 0:
                greenThread = ThreadID(greenCounter, curr_color)                
                thread = Thread(target = dressingRoom, args = [greenThread, n, curr_color,b,g])
                thread.start()
                
                handleGreenThreadsList.append(thread)
                i = i + 1
                g = g - 1
                greenCounter = greenCounter + 1
            
            for t in handleGreenThreadsList:
                t.join()
            curr_color = 'Blue'


if __name__ == '__main__':
    main()