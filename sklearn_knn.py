# Implementation KNN with sklearn
from sklearn.neighbors import KNeighborsClassifier
entradas, saidas = [], []

with open('haberman.data', 'r') as f:
	for linha in f.readlines():
		atrib = linha.replace('\n', '').split(',')
		entradas.append([int(atrib[0]), int(atrib[2])])
		saidas.append(int(atrib[3]))
print(saidas)