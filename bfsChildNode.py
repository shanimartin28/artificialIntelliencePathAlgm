import collections
import bfsNode
import sys

class bfsChildNode:
	"""BFS Child Node data"""

	def getChild(self,queueElement,colCount,rowCount):
                
                #print "Step9.1: In the getChild module "
		childNodesList=[]
		#print "Step9.2: queueElement-nodeId "
		#print queueElement.nodeId
		#print "Step9.3: queueElement-nodeState "
		#print queueElement.nodeState
		#print "Step9.4: colCount "
		#print colCount
                
		if queueElement.nodeId%int(colCount) == 0:
                   #print "Step9.5: Check condition 1- here if the node id is exactly divisible by col count- so right boundary"
                   #print "Step9.5.1: If the difference is greater or equal to - so we'l have the top element"
                   if queueElement.nodeId - int(colCount) >=1:
                       childNodesList.append(queueElement.nodeId - int(colCount))
                   #print "Step9.5.2: If node id is>1 the get the left element"
                   if queueElement.nodeId-1 >=1:
			childNodesList.append(queueElement.nodeId-1)
                   #print "Step9.5.3: Get the bottom element"
                   if queueElement.nodeId + int(colCount) <= int(rowCount) * int(colCount):
			childNodesList.append(queueElement.nodeId+int(colCount))
		elif queueElement.nodeId%int(colCount) == 1:
                        #print "Step9.6: Check condition 2- here left boundary"
			if queueElement.nodeId-int(colCount) >=1:
				childNodesList.append(queueElement.nodeId-int(colCount))
			if queueElement.nodeId+1 <= int(rowCount) * int(colCount):
				childNodesList.append(queueElement.nodeId+1)
			if  queueElement.nodeId + int(colCount) <= int(rowCount) * int(colCount):
				childNodesList.append(queueElement.nodeId+int(colCount))	
                else:
                        #print "Step9.7: Check condition 3"
			if queueElement.nodeId-int(colCount) >= 1: 
				childNodesList.append(queueElement.nodeId-int(colCount))
			if (queueElement.nodeId-1) >=1:
				childNodesList.append(queueElement.nodeId-1)
			if queueElement.nodeId+1 <= int(rowCount) * int(colCount):
				childNodesList.append(queueElement.nodeId+1)
			if queueElement.nodeId + int(colCount) <= int(rowCount) * int(colCount):
				childNodesList.append(queueElement.nodeId+int(colCount))


                #print "childNodesList at module level"
                #print childNodesList

                return childNodesList
		#sys.exit(0) 
		
		
		









	
