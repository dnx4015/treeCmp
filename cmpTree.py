import math

def createSpaces(nSpaces):
	space = "".join([" " for i in range(nSpaces)])
	return space

def cmpStr (i, j):
	return str(i)+":"+str(j)

class Node:
	def __init__(self, s):
		self.content = s
		self.sonLeft = None
		self.sonRight = None
		self.level = 0

	def __repr__(self):
		return self.content
	
	def left(self):
		return self.sonLeft
	
	def right(self):
		return self.sonRight
	
	def setLeft(self, node):
		self.sonLeft = node
		node.level = self.level + 1
	
	def setRight(self, node):
		self.sonRight = node
		node.level = self.level + 1

class Tree:
	def __init__(self, n):
		self.root = None
		self.nLevels = 1
		self.arr = [i for i in range(n)]
		self.lArrs = []
		self.n = n
		self.generate(n)

	def generate(self, n):
		if n == 1:
			arr = [self.arr[i] for i in range(self.n)]
			self.lArrs.append(arr)
		for c in range(n):
			self.generate(n-1)
			self.swap(0 if n % 2 else c, n-1)

	def swap(self, i, j):
		tmp = self.arr[i]
		self.arr[i] = self.arr[j]
		self.arr[j] = tmp

	def appendNode(self, node, parent, isLeft):
		if parent is not None:
			if isLeft:
				if parent.left() == None:
					parent.setLeft(node)
				else:
					node = parent.left()
			else:
				if parent.right() == None:
					parent.setRight(node)
				else:
					node = parent.right()
		else:
			if self.root == None:
				self.root = node
			else:
				node = self.root
		if node.level + 1 > self.nLevels:
			self.nLevels = node.level + 1
		return node

	def appendCmpNode(self, i, j, parent, side):
		node = Node(cmpStr(i, j))
		return self.appendNode(node, parent, side)
		
	def printTree(self):
		right = []
		self.printNode(self.root, 0, right)

	def printNode(self, node, level, right):
		line = ""
		for i in range(level-1):
			line += "   " if right[i] else " | "
		if level > 0:
			line += " \>"
		print line + (node.content if node != None else "---")
		if node != None and node.content.find(":") != -1:
			if level >= len(right):
				right.append(False)
			else:
				right[level] = False
			self.printNode(node.left(), level+1, right)
			right[level] = True
			self.printNode(node.right(), level+1, right)

