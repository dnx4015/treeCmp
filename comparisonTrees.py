from selectionSort import *
from mergeSort import *
from quickSort import *
from heapSort import *

SELECTION = 0
MERGE = 1
QUICK = 2
HEAP = 3

if __name__ == "__main__":
	n_vals = [3,4,8]
	for n in n_vals:
		for i in range(4):
			if i == SELECTION:
				print "SelectionSort Comparison Tree of ", n
				tree = SelectionSort(n)
			elif i == MERGE:
				print "MergeSort Comparison Tree of ", n
				tree = MergeSort(n)
			elif i == QUICK:
				print "QuickSort Comparison Tree of ", n
				tree = QuickSort(n)
			else:
				print "HeapSort Comparison Tree of ", n
				tree = HeapSort(n)
			tree.createCmpTree()
			tree.printTree()
			print ""
			print ""
	



