import pickle
import time


#calcula nota final. retorna [nota] e [bonus]
def nota_final(notas, faltas):
	
	bonus = 0
	nota = sum(notas)
	
	if faltas == 0:
		bonus = 2
		
	if nota == 99:
		bonus = 1
	if nota == 100:
		bonus = 0
		
	return nota, bonus
		

#funcao de ordenacao. retorna v, se m1 vem antes de m2.
def ordena_mat(m1, m2, dic):
	
	nome1, semestre1, notas1, faltas1 = dic[m1]
	nome2, semestre2, notas2, faltas2 = dic[m2]
	
	#soma a nota e o bonus
	nota_final1 = sum(nota_final(notas1, faltas1))
	nota_final2 = sum(nota_final(notas2, faltas2))
	
	
	if nota_final1 > nota_final2:
		return True
	else:
		return False
		
		

def main():
	startTime = time.time()
	
	#importar o dicionario do arquivo bin
	arquivo = open("entrada100.bin", "rb")
	
	dic = pickle.load(arquivo)
	
	lista_matriculas = []
	
	
	#criando a lista de matriculas não ordenada
	for matricula in dic:
		
		lista_matriculas.append(matricula)
		
	
	#ordenar a lista de uma vez
	for i in range(len(lista_matriculas)-1):
		
		for j in range(i+1, len(lista_matriculas)):
			
			if not ordena_mat(lista_matriculas[i], lista_matriculas[j], dic):
				lista_matriculas[i], lista_matriculas[j] = lista_matriculas[j], lista_matriculas[i]
	
	
	
	
	
	
	
	
	#cria um arquivo saida.txt
	#print quantidade de alunos aprovados (busca binaria)
	
	for i in lista_matriculas:
		print(i, dic[i])
	
	#tempo de execucao
	print('Tempo de execução =', time.time() - startTime)
	
if __name__=="__main__":
	main()
