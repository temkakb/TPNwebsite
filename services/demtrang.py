def demtrang(count):
    trang=""
    a=int(count/12)
    for i in range(1,a+1):
        trang +=str(i)
    if count %2!=0:
        trang +=str(a+1)
    return trang
def numtrang(numpage):
    staticnum=12
    end=numpage*staticnum
    start=numpage*staticnum-staticnum
    return [start,end]