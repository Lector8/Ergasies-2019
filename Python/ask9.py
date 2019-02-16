def maxSequence(l):

    m1 = l[0]
    m2 = l[0]
    arithmoi= [] 

    for i in range(1,len(l)):
        m2 = max(l[i], m2 + l[i])
        m1 = max(m1,m2) 
    print(m1,": ",end="")
    tmp = 0

    for i in range(0,len(l)):         
        if tmp == m1: 
                return(arithmoi)
        else:
            arithmoi.clear()
            tmp = 0
        for j in range(i,len(l)):
            tmp += l[j]
            arithmoi.append(l[j])
            if tmp == m1:
                break
                
print("Dwse me keno tous arithmous ths listas:")
l = list(map(int, input().split())) 

print(maxSequence(l))