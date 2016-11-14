from cmpTree import *

class Sort:
	def __init__(self, n):
		self.arr = []
		self.n = n
		self.tree = Tree(n)
		self.i = 0
		self.node = self.tree.root
		self.side = None
		self.indexes = [i for i in range(n)]

	def setArr(self, arr, i):
		self.arr = arr
		self.i = i
		self.node = None
		self.indexes = [i for i in range(self.n)]
	
	def isLess(self, i, j):
		tree = self.tree
		a, b = self.indexes[i], self.indexes[j]
		self.node = tree.appendCmpNode(a, b, self.node, self.side)
		left = self.arr[i] < self.arr[j]
		self.side = left
		return left 

	def swap(self, i, j):
		tmp = self.arr[i]
		self.arr[i] = self.arr[j]
		self.arr[j] = tmp
		tmp = self.indexes[i]
		self.indexes[i] = self.indexes[j]
		self.indexes[j] = tmp

	def realSort(self):
		return

	def sort(self):
		self.realSort()
		allStr = "".join(map(str, self.indexes))
		node = Node(allStr)
		self.tree.appendNode(node, self.node, self.side)
		
	def createCmpTree(self):
		l = len(self.tree.lArrs)
		for i in range(l):
			arr = self.tree.lArrs[i][:]
			self.setArr(arr, i)
			self.sort()

	def printTree(self):
		self.tree.printTree()



