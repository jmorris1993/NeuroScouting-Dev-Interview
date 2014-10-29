# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 15:37:56 2014

@author: jmorris
"""

"""
The way I approached this problem was to first create a list representation
of the values of the tree. Then convert the list representation to a tree
data structure.
"""

"""
Figuring out the pattern for ValueCalc
0:0         i:i
1:01        i:(i+1)/2-1,(i+1)/2
2:10        i:i/2,i/2-1
3:12        i:(i+1)/2-1,(i+1)/2
4:21        i:i/2,i/2-1
5:23        i:(i+1)/2-1,(i+1)/2
6:32        i:i/2,i/2-1
7:3         i:i/2-1
"""
"""Calculates the layer of the tree given a depth. Used recursion.
"""
def valueCalc(depth,alist):
    nextList = []
    if depth ==1:
        return alist
        
    for i in range(2*len(alist)):
        if i == 0:
            nextList.append(alist[0])
        elif i == 2*len(alist)-1:
            nextList.append(alist[-1])
            
        elif i != 2*len(alist)-1 and i%2 == 1:
            nextList.append(alist[(i+1)/2-1]+alist[(i+1)/2]) 
        
        else:
            nextList.append(alist[i/2]+alist[i/2-1])  

    return valueCalc(depth-1,nextList)



"""Creates the list representation of the values of the final tree.
"""

def finalListBuilder(depth):
    finalList = []
    for i in range(1,depth+1):
        for j in valueCalc(i,[1]):
            finalList.append(j)
        
    return finalList

    
"""Created a binary tree data structure, since Python doesn't have it built in.
"""
class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        return self.rightChild
        
    def getLeftChild(self):
        return self.leftChild
        
    def setRootVal(self,obj):
        self.key = obj
        
    def getRootVal(self):
        return self.key
    
    def __str__(self, depth=0):
        ret = ""

        # Print right branch
        if self.rightChild != None:
            ret += self.rightChild.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    "*depth) + str(self.key)

        # Print left branch
        if self.leftChild != None:
            ret += self.leftChild.__str__(depth + 1)

        return ret
  
  
"""Creates the tree from the list representation
I used the level order insert for this.
"""
def createTree(root, alist, start, size):
    left = 2*start+1
    right = 2*start+2
    
    if left > size or right > size:
        return;
    
    if root == None:
        tobj = BinaryTree(alist[start])
        root = tobj
        
    if root.getRightChild() == None and root.getLeftChild() == None:
        if left < size:
            root.insertLeft(alist[left])
        if right < size:
            root.insertRight(alist[right])
            
    createTree(root.getLeftChild(), alist, left, size)
    createTree(root.getRightChild(),alist, right, size)   
    
    
    
"""Main.
"""
def main(depth):
    if depth < 1:
        return None
    
    
    
    else:
        tree = BinaryTree(1)  
        finalList = finalListBuilder(depth)
        
        createTree(tree, finalList, 0, len(finalList))
        
        return tree

"""Change Arguments here. Will print to console.
"""
print main(5) 



"""Sample Output for print main(5)."""
"""
                1
            1
                4
        1
                4
            3
                6
    1
                6
            3
                7
        2
                7
            4
                8
1
                8
            4
                7
        2
                7
            3
                6
    1
                6
            3
                4
        1
                4
            1
                1

"""
    
    
    
    
    
    
    
    
    
    
    
        