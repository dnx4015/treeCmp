from cmpTree import *
from sort import *

class QuickSort(Sort):
	def partition(self, ini, end):
		i, j = ini, end-1
		while True:
			while i < end and self.isLess(i, end):
				i += 1
			while j > ini and self.isLess(end, j):
				j -= 1
			if i >= j : break
			self.swap(i, j)
			i, j = i + 1, j - 1
		self.swap(i, end)
		return i
			
	def realSort(self):
		stack = []
		stack.append((0, self.n-1))
		while len(stack) != 0:
			ini, end = stack.pop()
			if (end <= ini) : continue
			i = self.partition(ini, end)
			if i - ini > end - i:
				stack.append((ini, i-1))
				stack.append((i+1, end))
			else:
				stack.append((i+1, end))
				stack.append((ini, i-1))



if __name__ == "__main__":
	n = 3
	quick = QuickSort(n)
	quick.createCmpTree()
	quick.printTree()


