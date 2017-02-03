import random
def generate_list():
    alist = [x for x in range(random.randint(-10,10))]
    assert (len(alist)!=0), "alist not have value in array"
    assert (sum(alist)>0), "sum of alist < 0"
    return alist
    
def printIt():
    print( generate_list() )
    
def main():
    printIt()
    
if __name__ == '__main__':
    print("Test printIt():")
    main()
    
    

    
