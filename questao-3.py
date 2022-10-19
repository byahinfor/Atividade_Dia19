f1 = 0
f2 = 0
f3 = 3
f4 = 0
f5 = 0
for n in range(0,8):
    idada = int(input("Digite uma idade: "))
    if idade <= 15:
        idadae= fax1
    elif idade <= 30:
        idade = fax2
    elif idade <= 45:
        idade = fax3
    elif idade <= 60:
        idade = fax4
    else:
        idad = fax5
print(f"faixa etária 1 (até 15 anos ): {fax1}") 
print(f"faixa etária 2 (16 a 30 anos ): {fax2}")
print(f"faixa etária 3 (32 a 45 anos ): {fax3}")
print(f"faixa etária 4 (46 a 60 anos ): {fax4}")
print(f"faixa etária 5 (acima de 60 anos ): {fax5}")

print(f"Porcentagem de pessoas com até 15 anos:{fax1/8*100}%")
print(f"Porcentagem de pessoas acima de 60 anos:{fax5/8*100}%")
