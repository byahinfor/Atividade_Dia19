ingresso: float
quantidade: int
despesas: int
renda: float
lucro: float

import os

ingresso = 5
despesas = 200
quantidade = 120

os.system("cls")

while ingresso >= 1:
    renda = ingresso * quantidade
    lucro = renda - despesas
    print(f"|O preço do ingresso é: \t\t    {ingressos:.1f} |")
    print(f"|A quntidade de ingresssos vendidos é: \t    {quantidade} |") 
    print(f"|O lucro com essa quanidde de ingressos é: {lucro:.1f}|")
    print("=" *49)
    quantidade += 26
    ingresso-= 0.5
