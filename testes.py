def compararArquivos(arquivo1, arquivo2):                           #$ OK / Funcao para testes
    with open (arquivo1, 'r', encoding='utf-8') as ler:
        arq1 = ler.read()
    with open (arquivo2, 'r', encoding='utf-8') as ler:
        arq2 = ler.read()
    for i in range(len(arq1)):
        if arq1[i] != arq2[i]:
            print('erro: ', i)
            print(arq1[i:i + 30])
            break
    stringSaida = ('||' + '  ' + 'Saidas compativeis = ' + str(arq1 == arq2) + '  ' + '||')
    print('\t' + '=' * len(stringSaida))
    print('\t' + stringSaida)
    print('\t' + '=' * len(stringSaida))





'''
n1 = "Carolina Alves"
n2 = "João Teixeira"

print(n1 < n2)

def alfabetoSort(nome1, nome2):
	
	return nome1 < nome2
	
print(alfabetoSort(n2, n1))'''

from random import randrange


'''
lista = []
for i in range(50):
	lista.append(randrange(50, 80))
lista.sort()

print(lista)
'''


		










































