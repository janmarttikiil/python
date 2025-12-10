def upc(number):
    sum1=0
    sum2=0
    total=0
    checkdigit=0
    
    a=str(number).zfill(11)
    for x in range(0,11,2):
        sum1+=int(a[x])
    sum1=sum1*3
    for y in range(1,10,2):
        sum2+=int(a[y])
    total=sum1+sum2
    M=total%10
    if M!=0:
        checkdigit=10-M
    else:
        checkdigit=0
    return checkdigit

print(upc(12345678910))
print(upc(1234567))
print(upc(4210000526))
print(upc(3600029145))