from binarytree import heap
# Create a random max-heap
root = heap()
print('Max-heap of any height : \n',root)
# Create a random max heap of given height
root2 = heap(height=2)
print('Max-heap of given height : \n',root2)
# Create a random perfect min-heap of given height
root3 = heap(height=2,is_max=False,is_perfect=True)
print('Perfect min-heap of given height : \n',root3)