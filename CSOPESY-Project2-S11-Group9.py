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
    
    
    maxSlot.acquire() # Entry Section
    
    customersLeft = customersLeft - 1
    # Append a list of ThreadID objects that have arrived inside the dressing room
    if curr_color == 'Green':
        greenThreads.append(ThreadID)
    else:
        blueThreads.append(ThreadID)

    # Prints out the current color that was expected to arrive
    if ThreadID.color == curr_color:
        print(f'{ThreadID.color} {ThreadID.id}  has entered the dressing room')

        # If dressing room is empty
        if(customersInside == 0):
            print(f'{curr_color} only')

        customersInside = customersInside + 1

    # If max number of customer is reached inside the dressing room
    if ((customersInside == limit)):
            if curr_color == 'Blue':
                while(len(blueThreads) > 0):
                    # Prints out the threads inside the dressing room to indicate that they are leaving
                    
                    print(f'{blueThreads[0].color} {blueThreads[0].id} has left the dressing room')
                    
                    # Pops the first item in the list everytime to mantain order of arrival
                    blueThreads.pop(0)
                
                if b > 0: # As long as there are blue customers that left on a certain time period will print out to indicate the semaphore is free again
                    print('Dressing Room Empty...')
                # Release the semaphore
                maxSlot.release(customersInside)

            else:
                while(len(greenThreads) > 0):
                    print(f'{greenThreads[0].color} {greenThreads[0].id} has left the dressing room')
                    
                    # Pops the first item in the list everytime to mantain order of arrival
                    greenThreads.pop(0)
                    
                if g > 0: # As long as there are blue customers that left on a certain time period will print out to indicate the semaphore is free again
                    print('Dressing Room Empty...')
                # Release the semaphore
                maxSlot.release(customersInside) # Remainder Section
            
            # Empties out the dressing room                    
            customersInside = 0
        


    

def main():    
    n = int(input('Enter the number of slots in the fitting room:'))
    b = int(input('Enter the number of blue threads:'))
    g = int(input('Enter the number of green threads:'))

    global maxSlot
    
    # Creates a max space for the semaphore of size n
    maxSlot = BoundedSemaphore(n)


    # [0] Blue First, [1] Green First
    chooser = randint(2)
    
    global curr_color
    
    if (chooser == 1 and g > 0) or (chooser == 0 and (b <= 0 and g > 0)):
        curr_color = 'Green'
    elif (chooser == 0 and b > 0) or (chooser == 1 and (b > 0 and g <= 0 )):
        curr_color = 'Blue'

    # Creating ID numbers for blue and green threads
    blueCounter = 1
    greenCounter = 1
    
    # Number of remaining customers to enter the dressing room
    global customersLeft
    customersLeft = g + b
    
    # Determines how much customers are inside the dressing room
    global customersInside
    customersInside = 0
    
    # A list that will store the instances of each ThreadID ckass that will be created and will be sorted based on color
    global blueThreads, greenThreads
    blueThreads = []
    greenThreads = []
    
    # A list that will store the objects of each threading.Thread objects that will be created and will be sorted based on color

    handleBlueThreadsList = []
    handleGreenThreadsList = []


    while customersLeft > 0:
        i = 0
        if curr_color == 'Blue':
            # Check and see if there is still space on the dressing room and if there are remaining blue customers 
            while i < n and b > 0: 
                blueThread = ThreadID(blueCounter, curr_color)
                
                # Creates a thread 
                thread = Thread(target=dressingRoom, args = [blueThread, n, curr_color,b,g])
                # Runs the thread (make them enter the dressing room)
                thread.start()
                
                # Adds a small time delay to prevent mixing of colors inside the dressing room  
                time.sleep(1)
                handleBlueThreadsList.append(thread)
                
                i = i + 1
                b = b - 1
                blueCounter = blueCounter + 1
            
            for t in handleBlueThreadsList:
                # Ensures each thread currently stored in the list is terminated
                t.join()
                
            # Switches over to a new color to prevent starvation
            curr_color = 'Green'

        else:
            # Check and see if there is still space on the dressing room and if there are remaining green customers 
            
            while i < n and g > 0:
                greenThread = ThreadID(greenCounter, curr_color)                
                thread = Thread(target = dressingRoom, args = [greenThread, n, curr_color,b,g])
                # Runs the thread (make them enter the dressing room)
                thread.start()
                
                # Adds a small time delay to prevent mixing of colors inside the dressing room  
                time.sleep(1)
                handleGreenThreadsList.append(thread)
                i = i + 1
                g = g - 1
                greenCounter = greenCounter + 1
            
            for t in handleGreenThreadsList:
                # Ensures each thread currently stored in the list is terminated
                t.join()
            # Switches over to a new color to prevent starvation
            curr_color = 'Blue'



if __name__ == '__main__':
    main()