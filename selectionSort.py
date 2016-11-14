from cmpTree import *
from sort import *

class SelectionSort(Sort):
	def realSort(self):
		for i in range(self.n):
			minI = i
			for j in range(i+1, self.n):
				minI = j if self.isLess(j, minI) else minI
			self.swap(i, minI)

if __name__ == "__main__":
	n = 4
	select = SelectionSort(n)
	select.createCmpTree()
	select.printTree()

