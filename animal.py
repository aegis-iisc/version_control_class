import sys


def default():
    print("Hello to the SDF class")
def second():
    print ("Hello from the second branch")
def main():
    if sys.argv[1] == 'second':
        second()
    else:    
        default()
    
if __name__ == '__main__':
    main()    
    
    