import itertools 
sayilar=[]


while True:
    a = input("sayilar ->")
    if a =='k':
        break
    sayilar.append(int(a))

istenenSayi=int(input("istenen sayi ->"))
toplam = sum(sayilar)
print(toplam)


for i in range(1,len(sayilar)):
    liste=list(itertools.combinations(sayilar,i))
    for j in range(len(liste)):
        temp = toplam - sum(liste[j])*2
        
        #print(liste)
        if temp == istenenSayi:
            tempSayilar=sayilar
            
            print(liste[j])
            for k in range(len(liste[j][k])):
                if k in tempSayilar:
                    y=tempSayilar.index(k)
                    tempSayilar[y]=-tempSayilar[y]
            print(tempSayilar)
                    

    
