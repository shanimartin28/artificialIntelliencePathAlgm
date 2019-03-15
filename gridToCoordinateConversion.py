import collections
import bfsChildNode
import parentDict
import bfsNode
import sys

class gridToCoordinateConversion:
	"""BFS Node data"""
        nodeId=0
        nodeState=""
	rowCnt=0 
	colCnt=0 
	distance=0 
	parent=0 

	def aCoordRow(self,dictData,colCount,rowCount,linelist,child):
                            #print "kslajdlkjsadjkaskljdlksAJDLKSAJDKLjasdkljAJDKLAsjdkljsadkjadkjaskdjASLKDJKLASDJ"
                            #print ""
                            #print "child gottt::::::",child
                            totalNodes=int(rowCount)*int(colCount)
                            elementData={}
                            #print "From the line list just obain a count list"
                            countList=[]
                            for c in range(1,len(linelist)+1):
                                countList.append(c)
                            #print "Store element data in grid format"
                            startIndex=0
                            endIndex=int(colCount)
                            for k in range(0,int(rowCount)):
                                elementData[k]=bfsNode.bfsNode()
                                elementData[k].nodeState=linelist[startIndex:endIndex]
                                elementData[k].nodeId=countList[startIndex:endIndex]
                                startIndex=endIndex
                                endIndex=endIndex+int(colCount)
                            rowList=[]
                            rowList = elementData[0].nodeId

                            dictCoord={}
                            
                            for r in range(0,int(rowCount)):
                                rowList = elementData[r].nodeId
                                #print "row number:",r
                                #print "row values"
                                #print rowList
                                for c in range(1,len(rowList)+1):
                                        colVal=rowList[c-1]
                                        colNum=c-1
                                        #print "column number:",colNum
                                        #print "column value"
                                        #print colVal
                                        if int(child) == int(colVal):
                                            #print "COORDINATE VALUE FOR:",int(child)
                                            #coordVal="["+str(r)+","+str(colNum)+"]"
                                            #print coordVal
                                            return r
                                            
                            #return r
                

                
        def aCoordCol(self,dictData,colCount,rowCount,linelist,child):
                            totalNodes=int(rowCount)*int(colCount)
                            elementData={}
                            #print "From the line list just obain a count list"
                            countList=[]
                            for c in range(1,len(linelist)+1):
                                countList.append(c)
                            #print "Store element data in grid format"
                            startIndex=0
                            endIndex=int(colCount)
                            for k in range(0,int(rowCount)):
                                elementData[k]=bfsNode.bfsNode()
                                elementData[k].nodeState=linelist[startIndex:endIndex]
                                elementData[k].nodeId=countList[startIndex:endIndex]
                                startIndex=endIndex
                                endIndex=endIndex+int(colCount)
                            rowList=[]
                            rowList = elementData[0].nodeId

                            dictCoord={}
                            
                            for r in range(0,int(rowCount)):
                                rowList = elementData[r].nodeId
                                #print "row number:",r
                                #print "row values"
                                #print rowList
                                for c in range(1,len(rowList)+1):
                                        colVal=rowList[c-1]
                                        colNum=c-1
                                        #print "column number:",colNum
                                        #print "column value"
                                        #print colVal
                                        if int(child) == int(colVal):
                                            #print "COORDINATE VALUE FOR:",int(child)
                                            #coordVal="["+str(r)+","+str(colNum)+"]"
                                            #print coordVal
                                            #sys.exit(0)
                                            return colNum

                        
        def coordinateConverter(self,dictData,colCount,rowCount,linelist,bfsPath,algoStr):
                            #print "Step1: Find the nodes in each row"
                            #print "rowCount:",rowCount
                            #print "colCount:",colCount
                            totalNodes=int(rowCount)*int(colCount)
                            #print "total nodes:",totalNodes
                            #print "Data dict to hold element data in each row"
                            elementData={}
                            #print "So in each row -> col number of  elements are there"

                            #print "Step 2:From the line list just obain a count list"
                            countList=[]
                            for c in range(1,len(linelist)+1):
                                countList.append(c)
                            #print "linelist"
                            #print linelist
                            #print "countList"
                            #print countList   
                            
                            #print "Step 3: Store element data in grid format"
                            startIndex=0
                            endIndex=int(colCount)
                            for k in range(0,int(rowCount)):
                                #print "Row number-",k
                                #print "startIndex:"
                                #print startIndex
                                #print "endIndex"
                                #print endIndex
                                elementData[k]=bfsNode.bfsNode()
                                elementData[k].nodeState=linelist[startIndex:endIndex]
                                elementData[k].nodeId=countList[startIndex:endIndex]
                                #print "Row node state data"
                                #print elementData[k].nodeState
                                #print "Row node ids data"
                                #print elementData[k].nodeId
                                startIndex=endIndex
                                endIndex=endIndex+int(colCount)


                            #print "check get row 0,col 0"
                            rowList=[]
                            rowList = elementData[0].nodeId
                            #print rowList 
                            #print rowList[2]
                            
                            #print "Step4: Convert bfs path to coordinate system"
                            #print "bfsPath"
                            #print bfsPath
                            bfsPathCoord=[]

                            
                            
                            for k in range(1,len(bfsPath)+1):
                                bfsPathValue=bfsPath[k-1]
                                #print "bfsPath value:",bfsPathValue
                                for r in range(0,int(rowCount)):
                                    rowList = elementData[r].nodeId
                                    #print "row number:",r
                                    #print "row values"
                                    #print rowList
                                    for c in range(1,len(rowList)+1):
                                        colVal=rowList[c-1]
                                        colNum=c-1
                                        #print "column number:",colNum
                                        #print "column value"
                                        #print colVal
                                        if int(bfsPathValue) == int(colVal):
                                            #print "COORDINATE VALUE FOR:",int(bfsPathValue)
                                            #coordVal="["+str(r)+","+str(colNum)+"]"
                                            coordVal=""+str(r)+" "+str(colNum)+""
                                            print coordVal
                                            #bfsPathCoord.append(coordVal)
                                            #sys.exit(0)
                                        
                                         

                            
                            
                            
                            




                            
                            
