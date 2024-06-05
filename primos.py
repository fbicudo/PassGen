import time

primos = []
n = 5000

# for i in range(n,1,-1):
#     print(i)

print("-"*100)

t1 = time.time()

for i in range(2,n+1):
    # print(f"Testando o número {i}")
    occ = 0
    for d in range(1,i+1):
        # print(d)
        if i % d == 0:
            occ+=1
    if occ == 2:
        primos.append(i)

t2 = time.time()

print(primos)
print(f"Total execution time: {t2 - t1}")

