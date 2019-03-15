import collections
import bfsChildNode
import sys
import heapq
import costNode


class aStarNode:
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


        def numeric_compare(self,a, b):
                #print "hello"
                return cmp(a.nodeCost, b.nodeCost)
                #return x - y
	
        def __cmp__(a,b):
            return cmp(a.nodeCost, b.nodeCost)

                   
        
        def aStarAlgo(self,dictData,colCount,rowCount,linelist):
            #print "Start of A* algorithm"

            # priority queue to store nodes
            astar = []
            heapq.heapify(astar)
            i=1
            j=1
            pathTraversed = []
            wholePathTraversed = []
            childNodeRef=bfsChildNode.bfsChildNode()
            costNodeRef=costNode.costNode()
            #print "To find the key value for 's'"
            for i in range(1,len(dictData)+1):
                    if dictData[i].nodeState == 's':
                       key=dictData[i].nodeId
                       start=dictData[i]
                    if dictData[i].nodeState == 'g':
                       goalId=dictData[i].nodeId   


            #print "key",key
            #print "goalId",goalId
            # put the initial node on the queue
            #print "hello"
            heapq.heappush(astar, start)

            #print "Initial Value of queue:"
            #print astar
            #print ""

            tempList=[]
            stateList=[]
            startFlag=0
            aPath=[]
            lpath=[]

            while (len(astar) > 0):
            #while (len(astar)<3):
                    #print "Len of astar:"
                    #print len(astar)
                    
                    if len(astar)>= colCount :
                     sys.exit(0)
                    
                    queueElement=heapq.heappop(astar)
                    #print "OUTPUT VALUE"
                    #print "************"
                    #print "QueueElement: "
                    #print queueElement
                    #print "QueueElement:nodeState:"
                    #print queueElement.nodeState
                    #print "QueueElement:nodeId:"
                    #print queueElement.nodeId
                    #if queueElement.nodeCost!=0:
                        #print "QueueElement:nodeCost:"
                        #print queueElement.nodeCost
                        
                    
                   
                    nodeIdStr=str(queueElement.nodeId)
                    #print "nodeIdStr:"+nodeIdStr
                    if nodeIdStr not in tempList:
                            tempList.extend(nodeIdStr)
                    if nodeIdStr not in aPath:
                            aPath.append(nodeIdStr)

                    if queueElement.nodeState == 'g':
                            #print "Hello!!! goal acheived :)"
                            #print "The goal was found at node :",queueElement.nodeId
                            #print aPath
                            #print "apath:"
                            #print "^^^^^^"
                            for i in range(1,len(aPath)+1):
                                apathelem=aPath[i-1]
                                elem=dictData[int(apathelem)]
                                #print "Node:"
                                #print elem.nodeId
                                #print "NodeCost:"
                                #print elem.nodeCost
                                #print "NodeState:"
                                #print elem.nodeState
                                #print "______"
                            #sys.exit(0)
                            return aPath
                    else:
                            #print "Still long path to go, till now we have reached:"
                            #print tempList
                            #print "Create childBfsNodeList to store the child nodes"
                            childBfsNodeList=[]
                            #print "Call the getChild method module"
                            childBfsNodeList=childNodeRef.getChild(queueElement,colCount,rowCount)
                            #print "Children obtained"
                            #print childBfsNodeList
                            #print "For each child determine the cost for each child"
                            
                            costNodeRef.calcCost(childBfsNodeList,dictData,colCount,rowCount,linelist,goalId,key)
                            
                            
                            print ""
                            #print "ASTAR VALUES AFTER CHILD PROCESSING(SORT)"
                            #print "$$$$$$$$$$$$$$$$$$$$$$"
                            lep=[]
    
			    if len(childBfsNodeList)>0:
				for i in childBfsNodeList:
                                	if str(i) not in tempList:
                                                tempList.append(str(i))
                                                #if dictData[i].nodeState == "s":
                                                #       startFlag=1 
                                                #if startFlag==0:
                                                #        heapq.heappush(astar, dictData[i])
						#elif dictData[i].nodeState != "x":
                                                #        heapq.heappush(astar, dictData[i])
                                                #        lep.append(dictData[i].nodeCost)
                                                if dictData[i].nodeState != "x":
                                                        heapq.heappush(astar, dictData[i])
                                                        
                            
                            astar.sort(cmp=self.numeric_compare)
                                                
                            for i in range(1,len(astar)+1):
                                print ""
                                #print "Node:"
                                #print astar[i-1].nodeId
                                #print "NodeCost:"
                                #print astar[i-1].nodeCost
                                #print "______"
                            #if i==3:
                                    #sys.exit(0)




