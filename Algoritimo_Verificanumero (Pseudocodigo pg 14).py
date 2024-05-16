#Neste progama temos o objetuivo de verificar se o um NUMERO é maior que zero, menor que zero ou igual a zero.

#! inicio verifica numero.

numero = int(input("Digite um numero para verificar: "))

# analisamos o numero atraves da condicional if
 
if numero > 0: #condicional para numero maior que zero.
    print("o numero é positivo")
elif numero == 0: #Condicional para numero igual a zero.
    print("O numero é igual a zero")
else: #caso contrario o numero é negativo.
    print("o numero é negativo")
    
#! Encerra o progama
