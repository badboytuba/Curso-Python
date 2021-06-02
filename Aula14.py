numero = int(input("informe um numero: "))

if numero % 2 == 0:
    if numero > 0:
        print("o numero {0} e par e positivo".format(numero))
    else:  
        print("o numero {0} e par e negativo".format(numero)) 

else:
    if numero > 0:
        print("o numero {0} e impar e positivo".format(numero))    
    else:      
        print("o numero {0} e impar e negativo".format(numero))    