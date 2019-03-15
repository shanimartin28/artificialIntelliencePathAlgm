import collections
import bfsChildNode
import parentDict
import bfsNode
import sys

class bfsShortPathFinder:
	"""BFS Node data"""
        nodeId=0
        nodeState=""
	rowCnt=0 
	colCnt=0 
	distance=0 
	parent=0 

	
        def pathFinder(self,dictData,colCount,rowCount,linelist):
            #print "Step10.1: Start of Short Path Finder Game Algorithm"
            #print "***************************************************"
            shrtTrack=0
            #print ""
            i=1
            j=1
            bfsQueue = collections.deque()
            pathTraversed = []
            cnt = 0
            
            childNodeRef=bfsChildNode.bfsChildNode()
            parentRef=parentDict.parentDict()

            #print "Step8.1.1: To find the key value for 's'"
            for i in range(1,len(dictData)+1):
                    #print dictData[i].nodeState
                    if dictData[i].nodeState == 's':
                       key=dictData[i].nodeId
                       startkey=dictData[i]
                       #print "key=",key
           
            bfsQueue.append(startkey)

            tempList=[]
            stateList=[]
            startFlag=0
            bfsPath=[]

            parentDictData={}
            parentChildDictData={}

            keyList=[]
            shortGamePath=[]

            bfsNodeRef=bfsNode.bfsNode() 
            
            while bfsQueue:
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

                            
                            
                    if queueElement.nodeState == 'g':
                            shrtTrack=1
                            shrtpath=[]
                            #print "Hello!!! goal acheived :)"
                            #print "The goal was found at node :",queueElement.nodeId
                            #print bfsPath
                            #print "Step1: From the data dictionary find the key for the start position"
                            startKey=0
                            for i in range(1,len(dictData)+1):
                                if dictData[i].nodeState == 's':
                                   key=dictData[i].nodeId
                                   startKey=key
                            #print "Start key:",startKey
                            
                            childlist=[]
                            childlist=parentDictData.keys()
                            for i in range(1,len(childlist)+1):
                                    childID=childlist[i-1]
                                    
                                    #print "Parent:"
                                    #print parentDictData[childID].parentId
                                    #print "Child"
                                    #print childID
                                    #print "^^^^^^^^^^^^^^^^^^^"
                                    
                            goal=queueElement.nodeId
                            #print "goal",goal
                            #print "startKey",startKey

                            #print "Forming the shortest path by back tracking"
                            targetKey=goal
                            shrtpath.append(targetKey)
                            childID=targetKey
                            cnter=0
                            nextChildToCheck=0
                            while cnter<15:
                                            cnter=cnter+1
                                            if nextChildToCheck==0:
                                                    parentID=parentDictData[targetKey].parentId 
                                                    if parentID not in shrtpath:
                                                            shrtpath.append(parentID)
                                                    nextChildToCheck=parentID
                                                    #print "parentID cnter:",parentID
                                                    #print "shrtpath cnter:",shrtpath
                                                    #print "nextChildToCheck cnter:",nextChildToCheck
                                                    #sys.exit(0)
                                            else:
                                                 for i in range(1,len(childlist)+1):
                                                    #print "Start of backtracking"
                                                    childID=childlist[i-1]
                                                    if nextChildToCheck==childID:
                                                            parentID=parentDictData[nextChildToCheck].parentId
                                                            if parentID not in shrtpath:
                                                                    shrtpath.append(parentID)
                                                            nextChildToCheck=parentID
                                                            #print ""
                                                            #print "parentID for:",parentID
                                                            #print "nextChildToCheck for:",nextChildToCheck
                                                            #print "shrtpath so for:",shrtpath
                                                            #print ""


                            lenshrt=len(shrtpath)
                            #print "lenshrt",lenshrt
                            #print shrtpath[16]
                            srtCnt=1
                            bfsSrtPath=[]
                                                                
                            for i in range(1,len(shrtpath)+1):
                                  shrtVal=shrtpath[lenshrt-1]
                                  #print "Val in shrtpath",shrtVal
                                  bfsSrtPath.append(shrtVal)
                                  lenshrt=lenshrt-1  

                            #print bfsSrtPath        
                            
                            if shrtTrack==1:
                                return bfsSrtPath
                    
                
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
                            
                            #print "Step8.10: Store Parent Child Details"
                            j=1
                            parentNodeId=queueElement.nodeId
                            
                            for i in range(1,len(childBfsNodeList)+1):
                                    childNode=childBfsNodeList[i-1]
                                    if str(childNode) not in tempList:
                                            #print "11111111111111111-childNode",childNode
                                            parentDictData=parentRef.storeParent(parentNodeId,childNode,parentDictData)
                            #parentChildDictData=parentDictData
                            #print "222222222222-parentDictData"
                            #print parentDictData
                            childlist=[]
                            childlist=parentDictData.keys()
                            for i in range(1,len(childlist)+1):
                                    childID=childlist[i-1]
                                    #print ""
                                    #print "Parent:"
                                    #print parentDictData[childID].parentId
                                    #print "Child"
                                    #print childID
                                    #print ""
                                    #print "**************"

                            
                            #cnt = cnt +1
                            
                            #if cnt==3:
                            #        sys.exit(0)
                            
			    if len(childBfsNodeList)>0:
				for i in childBfsNodeList:
                                	if str(i) not in tempList:
                                                tempList.append(str(i))
                                                #if dictData[i].nodeState == "s":
                                                #       startFlag=1 
                                                #if startFlag==0:
                                                #        bfsQueue.append(dictData[i])
						#elif dictData[i].nodeState != "x":
                                                #        bfsQueue.append(dictData[i])
                                                if dictData[i].nodeState != "x":
                                                       bfsQueue.append(dictData[i])
                                                	
