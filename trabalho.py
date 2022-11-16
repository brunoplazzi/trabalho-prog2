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

#retorna True se s1 é mais recente que s2
def semestreSort(s1, s2):
	
	ano1, periodo1 = s1
	ano2, periodo2 = s2
	
	if ano1 > ano2:
		return True
	if ano1 < ano2:
		return False
	if periodo1 > periodo2:
		return True
	if periodo1 < periodo2:
		return False
		


# FUNCOES DE ORDENACAO

#retorna True, se m1 vem antes de m2
def antes(m1, m2, dic):
	
	nome1, semestre1, notas1, faltas1 = dic[m1]
	nome2, semestre2, notas2, faltas2 = dic[m2]
	
	nota1, bonus1 = nota_final(notas1, faltas1)
	nota2, bonus2 = nota_final(notas2, faltas2)
	
	#soma a nota e o bonus
	nota_final1 = nota1 + bonus1
	nota_final2 = nota2 + bonus2
	
	#verificacoes
	
	#compara notas totais
	if nota_final1 > nota_final2:
		return True
	if nota_final1 < nota_final2:
		return False
	
	#compara notas sem bonus	
	if nota1 > nota2:
		return True
	if nota1 < nota2:
		return False
	
	#compara semestre letivo
	
	if semestreSort(semestre1, semestre2):
		return True
	if not semestreSort(semestre1, semestre2):
		return False
	
	#ordem alfabética
	
	if nome1 < nome2:
		return True
	if nome1 > nome2:
		return False
	
	#ordem crescente de matricula
	
	if m1 < m2:
		return True
	if m1 > m2:
		return False
	

def merge(l, lEsq, lDir, dic):
	i = 0
	j = 0
	k = 0
	while i < len(lEsq) and j < len(lDir):
		if antes(lEsq[i], lDir[j], dic):
			l[k] = lEsq[i]
			i += 1
		else:
			l[k] = lDir[j]
			j += 1
		k += 1
	
	while i < len(lEsq):
		l[k] = lEsq[i]
		i += 1
		k += 1
	
	while j < len(lDir):
		l[k] = lDir[j]
		j += 1
		k += 1

def mergeSort(l, dic):
	
	if len(l) > 1:
		meio = len(l)//2
		lEsq = l[:meio]
		lDir = l[meio:]
		mergeSort(lEsq, dic)
		mergeSort(lDir, dic)
		merge(l, lEsq, lDir, dic)
		
#funcao que escreve no arquivo a saida
def cria_arquivo(lista_matriculas, dic):
	
	with open("saida.txt", "w") as f:
		
		for mat in lista_matriculas:
			
			nome, semestre, notas, faltas = dic[mat]
			
			soma_notas, bonus = nota_final(notas, faltas)
			
			if bonus == 0:
				linha = f"{nome} - {soma_notas}"
			
			else:
				linha = f"{nome} - {soma_notas} +{bonus}"
			
			f.write(linha)
			f.write("\n")
			
	#PERGUNTA PRO HILARIO DO \n****************************************************

def aprovados(lista_matriculas):
	print("APROVADOS")
	

def main():
	startTime = time.time()
	
	#importar o dicionario do arquivo bin
	arquivo = open("entrada100000.bin", "rb")
	
	dic = pickle.load(arquivo)
	
	lista_matriculas = []


	#criando a lista de matriculas não ordenada
	for matricula in dic:
		
		lista_matriculas.append(matricula)
		
	
	#ordenar a lista de uma vez
	mergeSort(lista_matriculas, dic)
	
	
	#cria um arquivo saida.txt
	cria_arquivo(lista_matriculas, dic)
		#PERGUNTA PRO HILARIO DO \n***************************************************************************
				

	#print quantidade de alunos aprovados (busca binaria)
	aprovados(lista_matriculas)
	
	
	#tempo de execucao
	print('Tempo de execução =', time.time() - startTime)
	#LEMBRA DE TIRAR ******************************************************************************************
	
	
	cont = 0
	for i in lista_matriculas:
		print(i, dic[i])
		cont +=1
		if cont == 100:
			break #LIMPA ESSA MERDA ************************************************************************
	
if __name__=="__main__":
	main()
