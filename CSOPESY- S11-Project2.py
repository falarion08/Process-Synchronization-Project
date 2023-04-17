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
    #print(f'amount of customers left: {customersLeft}')
    maxSlot.release()
    print(f'{ThreadID.color} {ThreadID.id}  has left the dressing room')

<<<<<<< Updated upstream
def dressingRoomOver(ThreadID):
    maxSlot.release()
    print(f'{ThreadID.color} {ThreadID.id}  has left the dressing room')

def main():
    n = int(input("Number of slots inside the fitting room: "))
    b = int(input("Number of blue threads: "))
    g = int(input("Number of green threads: "))
  
=======
    customersInside = customersInside + 1

    if (customersInside == limit or customersLeft == 0):
        if curr_color == 'Blue':
            while len(blueThreads) > 0:
                print(f'{blueThreads[0].color} {blueThreads[0].id} has left the dressing room')
                blueThreads.pop(0)
                customersInside -= 1
                maxSlot.release()
        else:
            while len(greenThreads) > 0:
                print(f'{greenThreads[0].color} {greenThreads[0].id} has left the dressing room')
                greenThreads.pop(0)
                customersInside -= 1
                maxSlot.release()

        print('Dressing Room Empty...')
            

def main():
    n = int(input('Enter the number of slots in the fitting room: '))
    b = int(input('Enter the number of blue threads: '))
    g = int(input('Enter the number of green threads: '))

>>>>>>> Stashed changes
    global maxSlot
    maxSlot = BoundedSemaphore(n)

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
            while i < n and b > 0:
                Thread(target=dressingRoom, args=[ThreadID(blueCounter, curr_color)]).start()
                i = i + 1
                b = b - 1
                blueCounter = blueCounter + 1
                if i == n and b > 0:
                  #Thread(target=dressingRoomOver, args=[ThreadID(blueCounter,curr_color)]).start
                  i = i - 1
            curr_color = 'Green'
        else:
            while i < n and g > 0:
                Thread(target=dressingRoom, args=[ThreadID(greenCounter, curr_color)]).start()
                i = i + 1
                g = g - 1
                greenCounter = greenCounter + 1
                if i == n and g > 0:
                  #Thread(target=dressingRoomOver, args=[ThreadID(greenCounter,curr_color)]).start()
                  i = i - 1
            curr_color = 'Blue'
        time.sleep(0.1)  # add a small delay to prevent busy waiting
    
    print('All customers have finished trying on clothes.')
    

if __name__ == '__main__':
    main()