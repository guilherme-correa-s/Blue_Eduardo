# 8.Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo
# vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []
print('==~~'*5)
for i in range(5):
    ida = int(input('Digite sua idade:\n'))
    alt = float(input('Digite sua altura:\n'))
    idade.append(ida)
    altura.append(alt)

idade.reverse()  ## Vira a lista ao contrario
altura.reverse()  ## Vira a lista ao contrario
print(idade)
print(altura)
print()
print('Fim do programa')
print('==~~'*5)
