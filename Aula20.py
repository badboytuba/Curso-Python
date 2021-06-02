maior = -999
menor = 999
soma  = 0

for n in range(1,11):
    valor = int(input("informe um valor: "))
    if valor >maior:
        maior = valor
    if valor < menor:
        menor = valor
    soma = soma + valor
else:
    valor = int(input("informe valor: "))
media = soma / 10

print("o maior numero e {0}".format(maior))
print("o menor numero e {0}".format(menor))
print("o media numero e {0}".format(media))