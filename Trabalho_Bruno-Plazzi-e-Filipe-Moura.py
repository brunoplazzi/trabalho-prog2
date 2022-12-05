#TRABALHO PROG2
#INTEGANTES:
#
#Bruno Schneider Plazzi - 20221BSI0072
#Filipe Anunciação Batista de Moura - 20221BSI0137



import pickle
import time

#retorna nota sem bonus e bonus
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

#retorna True, se s1 é mais recente que s2
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

#retorna True, se nome1 vem antes de nome2		
def alfabetoSort(nome1, nome2):
	
	return nome1 < nome2


#retorna True, se m1 vem antes de m2
def antes(m1, m2, dic):
	
	nome1, semestre1, notas1, faltas1 = dic[m1]
	nome2, semestre2, notas2, faltas2 = dic[m2]
	
	nota1, bonus1 = nota_final(notas1, faltas1)
	nota2, bonus2 = nota_final(notas2, faltas2)
	
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
	if semestre1 != semestre2:
		
		return semestreSort(semestre1, semestre2)
	
	#ordem alfabética
	if nome1 != nome2:
		if nome1 < nome2:
			return True
		if nome1 > nome2:
			return False
	
	#ordem crescente de matricula
	if m1 < m2:
		return True
	if m1 > m2:
		return False
	
#ordenacao com o mergeSort
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
		
#funcao que cria o arquivo de saida
def cria_arquivo(lista_matriculas, dic):
	
	with open("saida.txt", "w", encoding="UTF-8") as f:
		
		for mat in lista_matriculas:
			
			nome, semestre, notas, faltas = dic[mat]
			
			soma_notas, bonus = nota_final(notas, faltas)
			
			if bonus == 0:
				linha = f"{nome} - {soma_notas}"
			
			else:
				linha = f"{nome} - {soma_notas} +{bonus}"
			
			f.write(linha)
			f.write("\n")
			

#print no terminal a quantidade de alunos aprovados com busca binária
def buscaBin(media, l, dic):
	inicio, fim = 0, len(l)-1
	while inicio <= fim:
		meio = (inicio + fim)//2
		notas = dic[l[meio]][2]
		faltas = dic[l[meio]][3]
		if media == sum(nota_final(notas, faltas)): return meio
		if media < sum(nota_final(notas, faltas)): inicio = meio+1
		if media > sum(nota_final(notas, faltas)): fim = meio-1
	return -1

def aprovados(lista_matriculas, dic):
	
	media = 60
	
	pos_media = buscaBin(media, lista_matriculas, dic)
	
	while pos_media == -1 and media < 100:
		media +=1
		pos_media = buscaBin(media, lista_matriculas, dic)
	
	if media == 100 and pos_media == -1:
		print(0)
	else:
		
		while sum(nota_final(dic[lista_matriculas[pos_media +1]][2], dic[lista_matriculas[pos_media +1]][3])) == media:
			pos_media +=1
		
		print(pos_media +1)
	
def main():
	
	#importar o dicionario do arquivo bin
	arquivo = open("entrada.bin", "rb")
	
	dic = pickle.load(arquivo)
	
	#criando a lista de matriculas não ordenada
	lista_matriculas = []
	for matricula in dic:
		lista_matriculas.append(matricula)
	
	#ordenar a lista de uma vez
	mergeSort(lista_matriculas, dic)
	
	#cria um arquivo saida.txt
	cria_arquivo(lista_matriculas, dic)		

	#print quantidade de alunos aprovados (busca binaria)
	aprovados(lista_matriculas, dic)
	
if __name__=="__main__":
	main()
