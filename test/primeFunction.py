a = int(input("Enter a number:"))
def get_prime(a):
    for x in range(2,a):
        if a % x == 0:
            return False
        else:
            return True
        
        
        
if get_prime(a):
    print("It is a prime number")
else:
    print("It is not a prime number")
       
         
