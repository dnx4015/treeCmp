from cmpTree import *
from sort import *

class MergeSort(Sort):
	def realSort(self):
		aux = [0 for i in range(self.n)]
		auxindex = [0 for i in range(self.n)]
		self.splitMerge(0, self.n, aux, auxindex)


	def splitMerge(self, ini, end, aux, auxindex):
		if end - ini < 2: return
		mid = (ini + end)/2
		self.splitMerge(ini, mid, aux, auxindex)
		self.splitMerge(mid, end, aux, auxindex)
		self.merge( ini, mid, end, aux, auxindex)
		self.arr[ini:end] = aux[ini:end]	
		self.indexes[ini:end] = auxindex[ini:end]

	def merge(self, ini, mid, end, aux, auxindex):
		i, j = ini, mid
		for k in range(ini, end):
			if i < mid and (j >= end or self.isLess(i, j)):
				auxindex[k] = self.indexes[i]
				aux[k] = self.arr[i]
				i += 1
			else:
				auxindex[k] = self.indexes[j]
				aux[k] = self.arr[j]
				j += 1


if __name__ == "__main__":
	n = 4
	merge = MergeSort(n)
	merge.createCmpTree()
	merge.printTree()



