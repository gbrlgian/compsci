#Bem errado

def registrar():
	nome = input("Informe o nome do jogo: ")
	preco = input("Informe o preço do jogo: ")
	banco = {'nome':preco}
	return banco

def ordenarNome(dic, alg):
	lst = []
	lst2 = []
	ordDic = {} 
	lst = dic.items()

	if alg == "quick":
		lst2 = quicksort(lst, False)
		ordDic = lst2
		return ordDic

	elif alg == "bubble":
		lst2 = bubblesort(lst, False)
		ordDic = lst2
		return ordDic

	else: 
		return []

def ordenarPreco(dic, alg):
	lst= []
	lst2 = []
	ordDic = {} 
	lst = dic.items()

	if alg == "quick":
		lst2 = quicksort(lst, True)
		ordDic = lst2
		return ordDic

	elif alg == "bubble":
		lst2 = bubblesort(lst, True)
		ordDic = lst2
		return ordDic

	else: 
		return []

def quicksort(lista, num):
	if not lista:
			return []

	if num == True:
		
		return quicksort([(x[1] for x in lista[0:]
		if x[1:] < x[0]) + (x[1] for x in lista[0]) +
		(x[1] for x in lista[0:]
		if x[1:] >= x[0])], True)

	else:
		
		return quicksort([(x[0] for x in lista[0:]
		if x[1:] < x[0]) + (x[0] for x in lista[0]) +
		(x[0] for x in lista[0:]
		if x[1:] >= x[0])], False)

def bubblesort(lista, num):
	if not lista:
		return []

	if num == True:
		
		return(bubblesort([x[1] for x in lista[0:] 
		if x[1:] > lista[0:]], True))
	
	else:
	
		return(bubblesort([x[1] for x in lista[0:] 
		if x[1:] > lista[0:]], False))



ordenarNome(registrar(), "quick")
