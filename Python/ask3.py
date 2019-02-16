print("Dwse to filename")
fm = input()  
with open(fm) as f:
    Lines = f.readlines()

toPrint = ""
for x in Lines:
    ak = x
    for i in range(0,len(ak)):
        if ak[i]=='#':            
            toPrint +='\n'
            break
        else:
            toPrint += ak[i]           

print (toPrint,end='') 