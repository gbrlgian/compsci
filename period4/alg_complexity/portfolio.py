import json

with open('games.json', 'r') as file:
	games_dic = json.load(file)


def printDic(dic):

	for x in dic:
		print(list(dic.keys()))


def toList(dic, val):

	if not dic and val:
		return []

	lst = []

	if val.upper() == "NOME":
    
		for key in list(dic.keys()):
			lst.append([key])

	if val.upper() == "VALOR":
    
		for val in list(dic.values()):
    		lst.append([val])
	
	return lst


def partitionQuick(list, begin, end):
    pivot = list[begin]
    i = begin + 1
    j = end - 1
 
    while True:
        while (i <= j and list[i] <= pivot):
            i += 1

        while (i <= j and list[j] >= pivot):
            j -= 1
 
        if i <= j:
           list[i], list[j] = list[j], list[i]

        else:
            list[begin], list[j] = list[j], list[begin]
            return j


def quickSort(list, begin, end):

	if not lista:
    	print("Lista vazia.")
    	return []
  
	if end - begin > 1:
		p = partitionQuick(list, begin, end)
		quickSort(list, begin, p)
		quickSort(list, p + 1, end)
		

def merge(left_half, right_half):

    result_lst = []

    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            result_lst.append(left_half[0])
            left_half.remove(left_half[0])

        else:
            result_lst.append(right_half[0])
            right_half.remove(right_half[0])

    result_lst += right_half if len(left_half) == 0 else left_half

    return result_lst


def mergeSort(uns_list):

    if len(uns_list) <= 1:
        return uns_list
    
    middle = len(uns_list) // 2

    left_list = uns_list[:middle]
    right_list = uns_list[middle:]
    left_list = mergeSort(left_list)
    right_list = mergeSort(right_list)

    return list(merge(left_list, right_list))


printDic(games_dic)

def sorter(dic)

	val = input("Digite \"NOME\" para ordenar as entradas do dicionário por nome; \nOu, então, digite \"VALOR\" para ordernar as entradas por valor")
	games_lst = []
	games_lst = toList(games_dic, val)

	alg = input("Digite \"QUICK\" para ordenar o dicionário usando o algoritmo Quick Sort; \nOu, então, digite \"MERGE\" para ordernar o dicionário usando o Merge Sort.")
quickSort(games_lst, 0, len(games_lst))