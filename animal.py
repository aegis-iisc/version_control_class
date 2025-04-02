import sys


def default():
    print("Hello to the SDF class")
def first():
    print("Hello I am the first branch")
def second():
    print ("Hello from the second branch")  
def main():
    if sys.argv[1] == 'first':
        first()
    elif sys.argv[1] == 'second':
        second()
    else:    
        default()    
   
    
if __name__ == '__main__':
    main()    
    
    
