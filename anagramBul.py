paragraf = input("paragraf->" )

paragraf = paragraf.replace(".","")
paragraf = paragraf.replace(",","")
paragraf = paragraf.replace("!","")
paragraf = paragraf.replace("?","")
paragraf = paragraf.split(" ")

print(paragraf)

def karsilastir(kelime1, kelime2):
    if(sorted(kelime1) == sorted(kelime2)):
        return 1
    else:
        return 0


for i in range(len(paragraf)):

    #print(i)
    for a in range(i+1,len(paragraf)):
    #while a < len(paragraf):
        #print(a,i)
        isAnagram = karsilastir(paragraf[i], paragraf[a])
        if isAnagram:
            if paragraf[i] != paragraf[a]:
                print("anagram -> ",paragraf[i],paragraf[a])
            
    
        
                

