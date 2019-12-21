msg = input("paragraf ->")

sesliHarfler=['a','e','ı','i','o','ö','u','ü']

msg = msg.split(" ")

c = 0
for word in msg:
    c=1
    tempsesliHarfler=sesliHarfler
    for i in range(len(word)):
        if word[i] in sesliHarfler:
            if word[i] not in tempsesliHarfler:
                c=0
                break
            a = tempsesliHarfler.index(word[i])
            tempsesliHarfler = tempsesliHarfler[a:]
    if c:
        print(word)
            

        
            

