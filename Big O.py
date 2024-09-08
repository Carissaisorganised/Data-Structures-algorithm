def print_items(n):
    for i in range(n):
        
        print(i)
    
    print_items(10)
    
def print_items2(n): 
    for i in range(n):
        
        print(i)
        
        print_items2(14)
        