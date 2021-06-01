valor_por_hora = float(input("qual valor voce ganha por hora? "))
horas_trabalhadas = int(input("quantas horas voce trabalhou neste mes? "))

salario = horas_trabalhadas * valor_por_hora
print("neste mes voce vai receber R$ {0:.2f}".format(salario)) 