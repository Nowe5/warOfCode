matris=[]

def agacKoy(x,y):
    global matris
    matris.append([int(x),int(y)])
yol=""
enKucuk=10000
enYakinKonumAgac=[]
def enYakin(x,y):
    global enYakinKonumAgac
    global matris
    global enKucuk
    global yol
    t = 0
    if [x,y] in matris:
        print("ağaca uzaklık 0")
    else:
        for i in range(len(matris)):
            sayi=abs(matris[i][0]-int(x)) + abs(matris[i][1]-int(y))
            #print(sayi)
            if sayi < enKucuk:
                enKucuk = sayi
                yol = str(matris[i][0]-int(x)) + str(matris[i][1]-int(y))
                enYakinKonumAgac = matris[i]


while True:
    x=input("x")
    if int(x) ==-1:
        break
    y=input("y")
    agacKoy(x,y)
    
    
kx=input("kişi konumu x->")
ky=input("kişi konumu y->")

enYakin(kx,ky)

print("en yakın ağacım konumu",enYakinKonumAgac)
print("gidilecek kare sayisi",enKucuk)
print("x de gidilecek yol-y de gidilecek yol" ,yol)