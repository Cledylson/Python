"""01 - Implemente um programa que receba a idade de uma pessoa e imprima mensagem de
acordo com os critérios:
● Menor de 16 anos: MENOR
● Entre 16 e 18 anos: EMANCIPADO
● Maior de 18 anos: MAIOR

x = input("Coloque a idade ")
x = float(x)
if x <= 15:
    print("MENOR") 
elif x <= 16:
    print("EMANCIPADO")
elif x <= 17:
    print("EMANCIPADO")
elif x >= 18:
    print("MAIOR")

02 - Implemente um programa que receba a idade de um nadador e imprima a sua
categoria seguindo as regras
Categoria      idade

infantil  A     5 - 7 anos
infantil  B     8 - 10 anos 
juvenil  A      11 - 13 anos
juvenil  B      14 - 17 anos"""

x = input ( "Qual a idade do nadador(a) ?")
x = float(x)
if x in range (5,7):
    print(" Essa idade é da categoria infantil A")
    y = input ("Qual o nome do Nadador(a)?")
    print(f"Bem vindo {y}")
elif x in range (8,10):  
    print("Essa idade é da categoria infantil B")
    y = input ("Qual o nome do Nadador(a)?")
    print(f"Bem vindo {y}")
elif x in range(11,13):
    print("Essa idade é da categoria juvenil A")
    y= input ("Qual o nome do Nadador(a)?")
    print(f"Bem vindo {y}")
elif x in range (14,18):
    print("Essa idade é da categoria juvenil B ")
    y = input ("Qual o nome do Nadador(a)?")
    print(f"Bem vindo {y}")
else: 
    print("Não está dentro das idades das categorias suportadas")
