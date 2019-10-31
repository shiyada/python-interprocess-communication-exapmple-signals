import os 
import time
  
def parent_child(): 
    n = os.fork() 
  
    # n greater than 0  means parent process 
    if n > 0:
	time.sleep(5) 
        print("Parent process and id is : ", os.getpid()) 
  
    # n equals to 0 means child process 
    else: 
        print("Child process and id is : ", os.getpid()) 
          
# Driver code 
parent_child() 
