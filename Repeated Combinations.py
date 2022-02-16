a=0
for i in range(0,11):
    for j in range(0,11):
        for k in range(0,11):
            if i+j+k==10:
                print(i,j,k)
                a+=1
print(a)
                

            