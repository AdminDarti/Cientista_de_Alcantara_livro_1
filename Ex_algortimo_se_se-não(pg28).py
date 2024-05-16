


print("======================")
print("|Bem Vindo estudante!|")
print("======================")

print("exemplo basico do if(se) e else(senão)")

# Exemplo básico do uso do if e else

# Declaração de uma variável
idade = 18

# Verificando a condição usando o if
if idade >= 18:
    print("Você é maior de idade.")  # Se a condição for verdadeira, este bloco será executado.
else:
    print("Você é menor de idade.")  # Se a condição for falsa, este bloco será executado.


print("exemplo basico do if(se), else(senão) e elif(se-senão)")

# Exemplo com if, elif e else

# Declaração de uma variável
nota = 75

# Verificando a condição usando if, elif e else
if nota >= 90:
    print("Sua nota é A.")  # Se a condição for verdadeira, este bloco será executado.
elif nota >= 80:
    print("Sua nota é B.")  # Se a condição do if for falsa e a condição do elif for verdadeira, este bloco será executado.
elif nota >= 70:
    print("Sua nota é C.")  # Se as condições do if e do elif anteriores forem falsas e a condição deste elif for verdadeira, este bloco será executado.
elif nota >= 60:
    print("Sua nota é D.")  # Se as condições do if e dos elif anteriores forem falsas e a condição deste elif for verdadeira, este bloco será executado.
else:
    print("Sua nota é F.")  # Se todas as condições anteriores forem falsas, este bloco será executado.

