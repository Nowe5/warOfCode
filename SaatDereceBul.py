saatveDakika = input('saat')
if len(saatveDakika)<5:
    saat    = int(saatveDakika[0:1])
    dakika  = int(saatveDakika[2:4])
    #print(saat,dakika)
else:
    saat    = int(saatveDakika[0:2])%12
    dakika  = int(saatveDakika[3:5])
    #print(saat,dakika)

saat = 30*saat
dakika = 6*dakika

print(abs(saat-dakika))