#print('hi')


for a in range(1000) :
    
    if a < 10 :
        password = '00'+str(a)
    elif a < 100 :
        password = '0'+str(a)  
    else :
        password = a
    print(password)