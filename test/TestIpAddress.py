import socket
while("true"):
    web = input("Enter a website name:")
    ip = socket.gethostbyname(web)
    print(ip)
    
    if not ip:
        print("You entered an invalid website")
    else:
        print("The IP address is".format(ip))  
    
    cont = input("Do you want to continue? Press Y to continue")
    if  cont != 'Y':
            break 
        
        
    
    




   
    