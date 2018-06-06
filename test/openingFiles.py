#Python program to learn opening files
lines = []
myfile = open("C:\\Users\\priya\\tmp\\weekdays1.txt","r")
lines = myfile.readlines()
myfile.close
print(lines)


#Now I am going to use a method to reverse a list.
lines.reverse()
print(lines)
