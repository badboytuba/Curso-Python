valor_hora = 10
valor_horas_excedente = 20
e = 0

c = int(input("informe codigo: "))
n = float(input("informe a quantidade de horas trabalhadas: "))

if n > 50:
    e = (n - 50) * valor_horas_excedente
    salario = (50 * valor_hora) + e
    print("Salário com horas extras R$: {0:.2f}".format(salario))
    print("Valor Excedente Horas Extras R$:  {0:.2f}".format(e))
else:
    salario = (n * valor_hora)
    print("salario com horas extras R$: {0:.2f}".format(salario))
    print("Valor Excedente Horas Extras R$: {0:.2f}".format(e))