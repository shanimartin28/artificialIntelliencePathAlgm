import collections
import bfsChildNode
import sys

class bfsNode:
	"""BFS Node data"""
        nodeId=0
        parentId=0
        childId=0
        nodeState=""
	rowCnt=0 
	colCnt=0 
	distance=0 
	parent=0
	nodeCost=0
	
	
        def bfsAlgo(self,dictData,colCount,rowCount):
            #print "Step8.1: Start of BFS algorithm"
            i=1
            j=1
            bfsQueue = collections.deque()
            bfsKeyQueue = collections.deque()
            pathTraversed = []
            wholePathTraversed = []
            
            childNodeRef=bfsChildNode.bfsChildNode()
           
            #print "Step8.1.1: To find the key value for 's'"
            for i in range(1,len(dictData)+1):
                    #print dictData[i].nodeState
                    if dictData[i].nodeState == 's':
                       key=dictData[i].nodeId
                       startkey=dictData[i]
                       #print "key=",key

            #print "Step8.1.2:  To obtain the list from the start position 's'"
            i=key    
            for i in range(i,len(dictData)+1):
                    #print dictData[i].nodeId
                    #print dictData[i].nodeState
                    bfsKeyQueue.append(dictData[i])
                    
            
            #print "Step8.1.3:  bfsKeyQueue obtained"
            
            #print bfsKeyQueue

            #print "Step8.1.4: Initial value of bfsQueue:"
            #print ""
            #print bfsQueue
            #print ""
            #print "Dict data"
            #print dictData[j]
            #mod1
            #bfsQueue.append(dictData[j])
            bfsQueue.append(startkey)

            #print "Step8.1.5: Current Value of bfsQueue:"
            #print bfsQueue
            #print ""
            tempList=[]
            stateList=[]
            startFlag=0
            bfsPath=[]
            
            while bfsQueue:
            #for b in range(1,len(bfsQueue)+1):
                    #print "Len of bfsQueue"
                    #print len(bfsQueue)
                    
                    if len(bfsQueue)>= colCount :
                     sys.exit(0)
                    
                    queueElement=bfsQueue.popleft()
                    #print ""
                    #print "Step8.2: QueueElement: "
                    #print queueElement
                    #print "Step8.3: QueueElement:nodeState:"
                    #print queueElement.nodeState
                    #print "Step8.4: QueueElement:nodeId:"
                    #print queueElement.nodeId
                    nodeIdStr=str(queueElement.nodeId)
                    #print "nodeIdStr:"+nodeIdStr
                    if nodeIdStr not in tempList:
                            tempList.extend(nodeIdStr)
                    if nodeIdStr not in bfsPath:
                            bfsPath.append(nodeIdStr)

                    #sys.exit(0)       
                    if queueElement.nodeState == 'g':
                            #print "Hello!!! goal acheived :)"
                            #print "The goal was found at node :",queueElement.nodeId
                            #print bfsPath
                            return bfsPath
                    else:
                            #print "Step8.5: Still long path to go, till now we have reached:"
                            #print tempList
                            #print "Step8.6: Current status - bfsQueue elements"
                            #print bfsQueue
                            #print "Step8.7: Create childBfsNodeList to store the child nodes"
                            childBfsNodeList=[]
                            #print "Step8.8: Call the getChild method module"
                            childBfsNodeList=childNodeRef.getChild(queueElement,colCount,rowCount)
                            #print "Step8.9: Children obtained"
                            #print childBfsNodeList
			    if len(childBfsNodeList)>0:
				for i in childBfsNodeList:
                                	if str(i) not in tempList:
                                                #print "Hey i value:",i
                                                #print "Hey templist value:"
                                                #print tempList
                                                tempList.append(str(i))
                                                #print "Hey templist value after append:"
                                                #print tempList


                                                #mod2
                                                #if dictData[i].nodeState == "s":
                                                #       startFlag=1 
                                                #if startFlag==0:
                                                #        bfsQueue.append(dictData[i])
						#elif dictData[i].nodeState != "x":
                                                #        bfsQueue.append(dictData[i])

                                                if dictData[i].nodeState != "x":
                                                      bfsQueue.append(dictData[i])
                                                
                            #return bfsPath	
