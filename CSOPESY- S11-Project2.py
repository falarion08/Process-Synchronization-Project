import threading 
from threading import *
import numpy.random as npr

def main():
    n = int(input('Enter the number of slots in the fitting room:'))
    b = int(input('Enter the number of blue threads:'))
    g = int(input('Enter the number of green threads:'))
    
    maxSlots = BoundedSemaphore(n)

    blue_threads = Semaphore()
    green_threads = Semaphore() 
    
    # [0] Blue First, [1] Green First
    chooser = npr.randint(2)
    
    if (b and chooser == 0) or (g <= 0 and chooser == 1):
        firstColor = "Blue"
        bCnt = n
        gCnt = 0
        
        blue_ready = [True for i in range(b)]
        green_ready = [False for i in range(g)]
                

if __name__ == '__main__':
    main()