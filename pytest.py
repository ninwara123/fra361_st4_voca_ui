from object import login
file = open("user.txt","r")
for i in file:
    print(i)
    a,b = str(i).split(",")
    print(a+"\n"+b)
    if(a=="ytt" and b=="112233"):
        print("pass")
file.close()
