x=0
x1=1
x2=2
j=0  

while j < 4:
    xc=(x1+x2)/2
    x=xc
    fonk=x*x*x+4*x*x-10
    if(fonk<0):
        x1=xc
    else :
        x2=xc
    j += 1
print(" kok:")
print(xc)
print("buluanan deger:")
print(fonk)
