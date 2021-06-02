#numero igual que 0 true
maior = 0

n = int(input("informe o numero: "))
#numero maior a 0 false
while n != 0:
    if n > maior:
        maior = n
    n = int(input("informe o numero: "))
print("o maior numero e {0}".format(maior))                 