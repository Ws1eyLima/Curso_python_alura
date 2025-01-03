# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar 
# se o número é par ou ímpar

numero = int(input("Digite seu numero: "))

if numero % 2 == 0:
    print("Seu numero é par")
else:
    print("Seu numero é impar")

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

idade = int(input("Digite a sua idade: "))

if idade <= 12:
    print("Criança")
elif 13 >= idade <= 18:
    print("Adolecente") 
else:
    print("Adulto")

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar 
# se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.



user_name = input("Digite seu nome de usuario: ")
password = input("Digite sua senha: ")

if len(user_name) < 10 and len(password) < 10:
    print("login liberado")
else:
    print("Falha no login")