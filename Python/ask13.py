import sys

athr = [] 

def susums(l, a, b, sum = 0):     
    
    if a > b: 
        athr.append(sum)   
        return 
    
    susums(l, a + 1, b, sum + l[l]) 
    susums(l, a + 1, b, sum)

def calcsums(l):    
    mhkos = len(lista)
    athroismata = []
    for i in range(0,(1<<mhkos)):
        sum = 0
        for j in range(0,mhkos):
            if i & (1<<j):
                sum += l[j]
        athroismata.append(sum)
    print("to sum einai: ",athroismata)
    print ("to mhkos einai: ",len(athroismata))

def maxDistance(l, max):      
  susums(l,0,len(l)-1) 
  athr.sort(reverse=True) 
  isFound = False 
  for x in athr:
      if(x <= max and x != 0):
          print("max athroisma: ",x)
          isFound = True
          break
  if (isFound == False):
       print("O akereos  einai mikroteros apo ola ta athroismata")
 
print("Dwse me keno tous arithmous ths listas:")
l = list(map(int, input().split())) 
print("Dwse  thetiko akeraio")
max =  int(input())
if max < 0:
   print(" Dwste thetiko eipame")
   sys.exit()

maxDistance(l,max)
