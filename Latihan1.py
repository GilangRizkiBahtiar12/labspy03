print("Tampilkan n bilangan acak yang lebih kecil dari 0,5")

n = int(input("masukkan n: "))
import random
for i in range(n):
    print("data ke", i+1,"=",(random.uniform(0.1,0.5)))
