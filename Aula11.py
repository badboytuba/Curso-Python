p = float(input("informe o peso do peixe: "))

if p > 50:
    m = (p - 50) * 4.00
    e = 'excesso'
    print("Voce devera pagar de Multa por exesso o valor R$ {0:.2f}".format(m))
else:
    m = 0
    e = 0
    print("multas:{0}".format(m))
    print("excesso: {0}".format(e)) 
       
