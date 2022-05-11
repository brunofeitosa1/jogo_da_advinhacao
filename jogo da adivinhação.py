#Bruno Falcão Feitosa Massa Filho#
#1° Periodo - Sistemas da informação# 


print("jogo da adivinnhação!")


import random 
numero_aleatorio = random.randrange(0,100)
contador = 0
for i in range(0,100):
  contador += 1
  jogador = int(input("digite um numero:"))
  if(jogador == numero_aleatorio):
    print("jogador ganhou!")
    print(f"numero de tentativas foi: {contador}")
     
  else:
    print("Jogador errou!")
    if(jogador > numero_aleatorio ):
      print("numero maior que o sorteado:")
    elif(jogador < numero_aleatorio):   
      print("numero menor que o valor sorteado:") 
        
  


