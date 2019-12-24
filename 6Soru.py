import itertools 
sayilar=[]

while True:
    sayi = input("sayilar")
    if sayi == "k":
        break
    sayilar.append(int(sayi))

istenenSayi=int(input("istenen sayi->"))
    

for i in range(1,len(sayilar)+1):
    liste=list(itertools.combinations(sayilar,i))
    for j in range(len(liste)):
        if sum(liste[j]) == istenenSayi: 
            print(liste[j])

    


    