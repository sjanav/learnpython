a = ["1","5","9","7","6"]
b = ["1","5","10","8","7"]
c = []
for i in a:
    if i in b:
       c.append(i)
print("Overlap records are"+ str(c))
        
    
    