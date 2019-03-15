import collections
import bfsChildNode
import sys
import heapq
import gridToCoordinateConversion


class costNode:
	
        nodeId=0
        parentId=0
        childId=0
        nodeState=""
	rowCnt=0 
	colCnt=0 
	distance=0 
	parent=0
	nodeCost=0

	def G(self,currentX,currentY,startX,startY):
            # G is the cost of the node at that particluar level,we have assumed 10
            # At each advancement cost of G increases by 10
            answerG = 1*(abs(startX-currentX) + abs(startY-currentY))
            #print "Location:",currentX,currentY
            #print "answerG",answerG
            #answerG=10
            return answerG

        def H(self,currentX,currentY,targetX,targetY):
            # Hueristic function to determine how far the node is from the current location ignoring the wall in the way
            Hscore = 10*(abs(currentX-targetX) + abs(currentY-targetY))
            #print "Location:",currentX,currentY
            #print "Hscore",Hscore 
            return Hscore

        def F(self,currentX,currentY,targetX,targetY,startX,startY):
            # Total node cost
            Fscore = self.G(currentX,currentY,startX,startY) + self.H(currentX,currentY,targetX,targetY)
            #print "Location:",currentX,currentY
            #print "Fscore",Fscore 
            return Fscore
	
        def calcCost(self,childBfsNodeList,dictData,colCount,rowCount,linelist,goalId,startkey):
            #print "Start cost calc"
            coordinateRef=gridToCoordinateConversion.gridToCoordinateConversion()
            #print "goalId",goalId
            
            rowgoalId=coordinateRef.aCoordRow(dictData,colCount,rowCount,linelist,goalId)
            #print "rowgoalId",rowgoalId
            colgoalId=coordinateRef.aCoordCol(dictData,colCount,rowCount,linelist,goalId)
            #print "colgoalId",colgoalId

            targetX=rowgoalId
            targetY=colgoalId

            rowstartkey=coordinateRef.aCoordRow(dictData,colCount,rowCount,linelist,startkey)
            #print "rowstartkey",rowstartkey
            colstartkey=coordinateRef.aCoordCol(dictData,colCount,rowCount,linelist,startkey)
            #print "rowstartkey",rowstartkey

            startX=rowstartkey
            startY=colstartkey
            
           
            for i in range(1,len(childBfsNodeList)+1):
                child=childBfsNodeList[i-1]

                #print "child",child
                
                row=coordinateRef.aCoordRow(dictData,colCount,rowCount,linelist,child)
                #print "row",row
                currentX=row

                col=coordinateRef.aCoordCol(dictData,colCount,rowCount,linelist,child)
                #print "col",col
                currentY=col
                #print "Location:",currentX,currentY
                totCost=self.F(currentX,currentY,targetX,targetY,startX,startY)
                #print "totCost:",totCost
                dictData[child].nodeCost=totCost
                #print "dictData[child].nodeCost",dictData[child].nodeCost
                #print "&&&&&&&&&&&&&&&&"
                
            #sys.exit(0)
            return dictData      
