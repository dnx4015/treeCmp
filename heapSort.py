from cmpTree import *
from sort import *

class HeapSort(Sort):	
	def realSort(self):
		self.heapfy()
		for k in range(self.n-1, 0, -1):
			self.swap(k, 0)
			self.fixdown(0, k)

	def heapfy(self):
		for i in range(self.n/2, -1, -1):
			self.fixdown(i, self.n)
		
	def fixdown(self, k, n):
		son = 2 * k + 1
		while son < n:
			if (son + 1) < n and \
				self.isLess(son, son+1):
				son += 1
			if self.isLess(k,son):
				self.swap(k, son)
				k = son
				son = 2 * k + 1
			else:
				break
		return k



if __name__ == "__main__":
	n = 3
	heap = HeapSort(n)
	heap.createCmpTree()
	heap.printTree()
