import threading
from threading import *
from numpy.random import *

z = None
threads_inside = 0

class threadID:
    def __init__(self, id, color):
        self.id = int(id)
        self.color = color
        
        



def main():
    n = int(input('Enter the number of slots in the fitting room:'))
    b = int(input('Enter the number of blue threads:'))
    g = int(input('Enter the number of green threads:'))
    
    maxSlots = BoundedSemaphore(n)

    semaphore = Semaphore()
    
    # [0] Blue First, [1] Green First
    chooser = randint(2)
    
    # if (chooser == 0 and b > 0) or (chooser == 1 and b < 0):
        

if __name__ == '__main__':
    main()