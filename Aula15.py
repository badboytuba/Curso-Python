indice = float(input("informe o indice da poluição: "))

if indice >= 0.3 and indice < 0.4:
    print("atencao:indrustias do 10 grupo devem suspeder as atividade. ")
elif indice >= 0.4 and indice < 0.5:
    print("atencao:indrustias do 10 e 20 grupo devem suspeder as atividade. ")
elif indice >= 0.5:
    print("atencao: Todos os grupos devem suspeder as atividade. ")   
elif indice < 0.3:
    print("Ninguem Para ")
    


