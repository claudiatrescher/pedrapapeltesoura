pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



import random

humano = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura\n"))
print("Você escolheu:")
if humano == 0:
  print(pedra)

elif humano == 1:
  print(papel)

else:
  print(tesoura)


print("O computador escolheu:")
computador = random.randint(0,2)
if computador == 0:
  print(pedra)
elif computador == 1:
  print(papel)
else:
  print(tesoura)




jogo = [humano, computador]

if jogo[0] == jogo[1]:
  print("Está empatado!" )

elif jogo == [0,1] or jogo == [1,2] or jogo == [2,0]:
  print("Você perdeu!")

else:
  print("Você ganhou!")

