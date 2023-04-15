import threading
from threading import *
from numpy.random import *

class ThreadID:
    def __init__(self, id, color):
        self.id = id
        self.color = color
        self.thread = Thread(target=dressingRoom, args = [id,color])
        
def dressingRoom(thread_id, thread_color):
    maxSlot.acquire()
    print(f'ID: {thread_id} {thread_color} has entered the fitting room')
    maxSlot.release()

def handleBlueThreads(blueThreads):
    print(blueThreads)

def main():
    n = int(input('Enter the number of slots in the fitting room:'))
    b = int(input('Enter the number of blue threads:'))
    g = int(input('Enter the number of green threads:'))

    global maxSlot
    maxSlot = BoundedSemaphore(n)

    global semaphore
    semaphore = Semaphore()


    # [0] Blue First, [1] Green First
    chooser = randint(2)

    if chooser == 1:
        curr_color = 'Green'
    else:
        curr_color = 'Blue'

    blueThreads = []
    greenThreads = []

    blueCounter = 1
    greenCounter = 1

    while(b > 0 and g > 0):
        if curr_color == 'Blue':
            i = 0
            while(i < n):
                if b == 0:
                    break
                blueThreads.append(ThreadID(blueCounter, 'Blue'))
                blueThreads[blueCounter-1].thread.start()
                i = i + 1
                blueCounter = blueCounter + 1
                b = b - 1
                
            handleBlueThreads(blueThreads)
        else:
            i = 0
            while(i < n):
                if g == 0:
                    break
                greenThreads.append(ThreadID(greenCounter, 'Green'))

                greenThreads[greenCounter - 1].thread.start()
                i = i + 1
                greenCounter = greenCounter + 1
                g = g - 1
                


if __name__ == '__main__':
    main()