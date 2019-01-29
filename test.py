import random

from bst import Node, Tree

if __name__ == "__main__":
    population = [i for i in range(1, 1000)]
    nums = random.sample(population, 10)
    bst = Tree(nums)
    bst.inorder_print()
    #node = bst.search(nums[1])
    #print(node.val)
    #bst.insert(500)
    #bst.inorder_print()
    print('***')
    node = bst.search(nums[6])
    print(node.left.val, node.right.val)
    bst.delete(nums[6])
    bst.inorder_print()