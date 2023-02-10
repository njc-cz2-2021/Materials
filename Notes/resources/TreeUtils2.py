''' 
MIT License

Copyright (c) 2023 NJC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

## The code here works with Nodes with get_data(), get_left(), get_right() attributes

## Use print_tree to display a 2-D view if a BST by passing in the root node of the tree
def print_tree(root):
    ## complete is a list of levels in a tree level 0 is a list containing the root
    ## level 1 is a list containing 2 nodes , etc
    ## number of levels(height of tree) is floor( log2(number of nodes in tree))
    
    complete = bf_traversal(root)
    h = len(complete)
    ws = (2**h)-1

    def printSpace(n):
        for _ in range(n):
            print(" ", end="")
    for level in complete:
        ws = ws //2
        for i, x in enumerate(level):
            if i == 0:
                printSpace(ws)
            if x == None:
                x = " "
            print(x, end="")
            printSpace(1+2*ws)
        print()

## helper for print_tree
def bf_traversal(root)->list:
    ## root is a node with data,left and right attributes
    ## returns a complete binary tree
    ## Breadth First traversal
    ## Traverse list while appending to it

    cur_level = [root]
    next_level = []
    complete = [] ## complete tree , containing a list for level 0,1, ..n 
                    ## the number of nodes in each level is a GP, 1,2,4,8,..2^n
    while True:
        level=[]
        for node in cur_level:
            if node :
                level.append(node.get_data())
                if node.get_left() :
                    next_level.append(node.get_left())
                else:
                    next_level.append(None)

                if node.get_right():
                    next_level.append(node.get_right())
                else:
                    next_level.append(None)
            else: # leaf node
                level.append(None)
                next_level.append(None)
                next_level.append(None)
        complete.append(level)
        if any ( next_level):
            cur_level = next_level
            next_level = []
        else:
            ## next level has no nodes
            break    
    return complete


def gen_inOrder(root): # returns a sequence of node.data
    stack = []
    if root:
        stack.insert(0,root)
        T = type(root) ## Node type is not defined here
    while stack:
        cur = stack.pop(0)
        if type(cur) == T:
            if cur.get_right :
                stack.insert(0, cur.get_right())
            stack.insert(0,cur.get_data())
            if cur.get_left():
                stack.insert(0, cur.get_left())
        else:
            yield(cur)

## returns a order of nodes to be inserted such that they will be balanced 
def balanced_order( sorted_list:list): # returns a sequence in balanced order
    if len(sorted_list) == 0:
        return
    mid=len(sorted_list)//2
    yield (sorted_list[mid])
    yield from balanced_order (sorted_list[:mid])
    yield from balanced_order (sorted_list[mid+1:])

## needs to pass in an empty BST
def re_balance(unbalanced_tree, balanced_tree): ## returns a balanced BST
    for data in balanced_order ( list(gen_inOrder(unbalanced_tree.root)) ):
        balanced_tree.insert(data)
    return balanced_tree 

def calc_depth(root):
    if root == None:
        return 0
    left_depth = calc_depth( root.get_left() ) if root.get_left() else 0
    right_depth = calc_depth( root.get_right() ) if root.get_right() else 0
    return max ( left_depth, right_depth) + 1 
def is_balanced(root):
    if root == None:
        return True

    if abs( calc_depth(root.get_left()) - calc_depth(root.get_right()) ) <= 1 and \
       is_balanced( root.get_left()) and is_balanced(root.get_right()):
       return True

    return False 
        