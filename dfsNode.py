import collections
import bfsChildNode
import sys


class dfsNode:
	"""BFS Node data"""
        nodeId=0
        parentId=0
        childId=0
        nodeState=""
	rowCnt=0 
	colCnt=0 
	distance=0 
	parent=0 
	
	
        def dfsAlgo(self,dictData,colCount,rowCount):
            #print "Start of DFS algorithm"
            i=1
            j=1
            pathTraversed = []
            wholePathTraversed = []
            childNodeRef=bfsChildNode.bfsChildNode()
            #print "To find the key value for 's'"
            for i in range(1,len(dictData)+1):
                    #print dictData[i].nodeState
                    if dictData[i].nodeState == 's':
                       key=dictData[i].nodeId
                       strtkey=dictData[i]
                       #print "key=",key
            stack=[]
            #stack.append(dictData[j])
            stack.append(strtkey)
            #print "Current Value of stack:"
            #print stack
            #print ""
            tempList=[]
            stateList=[]
            startFlag=0
            bfsPath=[]
            
            while stack:
                    #print "Len of stack:"
                    #print len(stack)
                    
                    if len(stack)>= colCount :
                     sys.exit(0)
                    
                    queueElement=stack.pop()
                    #print ""
                    #print "QueueElement: "
                    #print queueElement
                    #print "QueueElement:nodeState:"
                    #print queueElement.nodeState
                    #print "QueueElement:nodeId:"
                    #print queueElement.nodeId
                    nodeIdStr=str(queueElement.nodeId)
                    #print "nodeIdStr:"+nodeIdStr
                    if nodeIdStr not in tempList:
                            tempList.extend(nodeIdStr)
                    if nodeIdStr not in bfsPath:
                            bfsPath.append(nodeIdStr)

                    if queueElement.nodeState == 'g':
                            #print "Hello!!! goal acheived :)"
                            #print "The goal was found at node :",queueElement.nodeId
                            #print bfsPath
                            #sys.exit(0)
                            return bfsPath
                    else:
                            #print "Still long path to go, till now we have reached:"
                            #print tempList
                            #print "Current status - stack elements"
                            #print stack
                            #print "Create childBfsNodeList to store the child nodes"
                            childBfsNodeList=[]
                            #print "Call the getChild method module"
                            childBfsNodeList=childNodeRef.getChild(queueElement,colCount,rowCount)
                            #print "Children obtained"
                            #print childBfsNodeList
			    if len(childBfsNodeList)>0:
				for i in childBfsNodeList:
                                	if str(i) not in tempList:
                                                tempList.append(str(i))
                                                #if dictData[i].nodeState == "s":
                                                #       startFlag=1 
                                                #if startFlag==0:
                                                #        stack.append(dictData[i])
						#elif dictData[i].nodeState != "x":
                                                #        stack.append(dictData[i])
                                                if dictData[i].nodeState != "x":
                                                        stack.append(dictData[i])
        
