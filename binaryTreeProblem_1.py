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

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        