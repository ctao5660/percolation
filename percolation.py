#! /usr/local/bin/python3.6
import random
class Percolation:
    def __init__(self,size): #size is the length or width of the array, must be a square
        self.size=size
        self.grid=[[0 for x in range(size)]for y in range(size)]
        self.algorithm=Quick_Find(size**2+2)  #size**2+1 will be end root node , size**2 will be start root node
        self.startNode=size**2
        self.endNode=size**2+1
        for i in range(size): #setting all start nodes to link to same node
            self.algorithm.union(self.oneD(0,i),self.startNode)
        for i in range(size): #setting all end nodes ot link to same node
            self.algorithm.union(self.oneD(size-1,i),self.endNode)
    def open(self,row,column):
        """sets each empty square in the grid to a 1 to indicate it has been opened, then .union the grid square with all other open grid squares in proximity.""" 
        self.grid[row][column]=1
        r=row-1
        c=column
        try:
            if(self.isOpen(r,c)):
                self.algorithm.union(self.oneD(row,column),self.oneD(r,c))
        except IndexError:
            None
        r+=1
        c-=1
        try:
            if(self.isOpen(r,c)):
                self.algorithm.union(self.oneD(row,column),self.oneD(r,c))
        except IndexError:
            None
        c+=2
        try:
            if(self.isOpen(r,c)):
                self.algorithm.union(self.oneD(row,column),self.oneD(r,c))
        except IndexError:
            None
        c-=1
        r+=1
        try:
            if(self.isOpen(r,c)):
                self.algorithm.union(self.oneD(row,column),self.oneD(r,c))
        except IndexError:
            None
    def isPercolated(self):
        """returns if the start node is connected to the end node (see constructor for more information)"""
        return self.algorithm.isConnected(self.startNode,self.endNode)

    def isOpen(self,row,column):
        if(row<0 or row>self.size or column<0 or column>self.size):
            return False
        if(self.grid[row][column]==1):
            return True
        else:
            return False
    def oneD(self,row,column):
        """converts 2D array coordinates to 1D array coordinates"""
        print('   ',row,column)
        return row*self.size+column
class Percolation_Tester:
    def __init__(self,size):
        self.size=size
        self.avg=[]
    def runTests(self,numTests):
        """runs percolation tests by picking random grid squares to open and returns the average ratio of open grid squares to total grid squares, each test ends the second it percolates"""
        for i in range(numTests):
            opened=0
            percolate=Percolation(self.size)
            while( not percolate.isPercolated()):
                randNumX=random.randint(0,self.size-1)
                randNumY=random.randint(0,self.size-1)
                if(not percolate.isOpen(randNumX,randNumY)):
                        percolate.open(randNumX,randNumY)
                        opened+=1
            self.avg.append(opened/self.size**2)
        return sum(self.avg)/len(self.avg)
class Quick_Find:
    """quick find algorithm involving tree log2(n) complexity"""
    def __init__(self,num_items):
        self.tree=[i for i in range(num_items)]
        self.size={}
        for i in range(len(self.tree)):
            self.size[i]=1
    def union(self,item1,item2):
        """connects two different items by taking the root node of the lesser sized tree and pointing it to the root node of the greater sized tree"""
        if(self.size[item1]>self.size[item2]):
            self.tree[self.findRoot(item2)]=self.tree[self.findRoot(item1)]
            self.size[item1]+=self.size[item2]
        else:
            self.tree[self.findRoot(item1)]=self.tree[self.findRoot(item2)]
            self.size[item2]+=self.size[item1]

    def findRoot(self,item):
        """recursive function that returns the root of a given item by following it up the tree. At the same time, the algorithm point a node to its grandparent to reduce the depth of the tree"""
        if(self.tree[item]==item):
            return item
        else:
            self.tree[item]=self.tree[self.tree[item]] #setting each root to it's grandparent to reduce depth  of tree
            return self.findRoot(self.tree[item]) #moves one layer up
    def isConnected(self,item1,item2):
        """returns whether the two items are connected by comparing their root nodes. If their root nodes are the same, then they are connected."""
        if(self.findRoot(item1)==self.findRoot(item2)):
            return True
        else:
            return False


percocet=Percolation_Tester(20)
print(percocet.runTests(5))

        

