file = open("EventGuest.txt","w")
names = input("enter names to invite ")
while names != "No":
    file.write(names + "\n")
    names = input("enter names to invite ")
file.close()
file = open("EventGuest.txt","r")
data = file.read()
print (data)
