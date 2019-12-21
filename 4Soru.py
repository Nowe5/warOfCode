import time



def sifrele(x):
    sec=int(time.strftime("%S"))%9
    sec=sec+1
    x = int(x)
    sayi = sec*x*1111
    return str(sec)+str(sayi)

def desifrele(x):
    sec = int(x[0])
    sayi = int(x[1:])
    sayi = sayi/(1111*sec)
    return str(sayi)

while True:
    x = input("sifrele ->")
    girdi = sifrele(x)
    print(girdi)
    y = input("desifrele ->")
    cikti = desifrele(y)
    print(cikti)