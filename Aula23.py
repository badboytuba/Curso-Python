contador_total = 0
contador_sit_1 = 0
contador_sit_2 = 0
contador_sit_3 = 0
contador_sit_4 = 0

indentificador = int(input("informa a indentificasao: "))

while indentificador != 0:
    print("1 - nesesidade de esfera.")
    print("2 - nesesidade de lane.")
    print("3 - nesesidade trocar cabo conector.")
    print("4 - quebrado ou inutilisado.")
    defeito = int(input("informe o tipo de defeito: "))

    if defeito == 1:
        contador_sit_1 = contador_sit_1 + 1
    elif defeito == 2:
        contador_sit_2 = contador_sit_2 + 1
    elif defeito == 3:
        contador_sit_3 = contador_sit_3 + 1    
    elif defeito == 4:
        contador_sit_4 = contador_sit_4 + 1
    contador_total = contador_total + 1
    indentificador = int(input("informa a indentificasao: "))
p1 = contador_sit_1 / contador_total * 100.0
p2 = contador_sit_2 / contador_total * 100.0
p3 = contador_sit_3 / contador_total * 100.0
p4 = contador_sit_4 / contador_total * 100.0
print("situasao                      quantidade                    precentual")
print("1 - nesesidad da esfera                        {0}                  {1:.2f}%".format(contador_sit_1, p1))
print("2 - nesesidad da limpeza                       {0}                  {1:.2f}%".format(contador_sit_2, p2))
print("3 - nesesidad da troca do cabo                 {0}                  {1:.2f}%".format(contador_sit_3, p3))
print("4 - quebrado ou unitilizado                    {0}                  {1:.2f}%".format(contador_sit_4, p4))