print("Laba Inventasi")

m = int(input("Uang Modal Awal: "))

a = 0*m
b = 0*m
c = 0.01*m
d = 0.01*m
e = 0.05*m
f = 0.05*m
g = 0.05*m
h = 0.02*m
y=[a,b,c,d,e,f,g,h]

for i in range(len(y)):
    print("Laba Bulan Ke",i+1 ,"sebesar: ",y[i])

z=(a+b+c+d+e+f+g+h)
print("Jumlah Laba Selama 8 Bulan: ",z)