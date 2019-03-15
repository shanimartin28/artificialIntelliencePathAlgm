import sys
import readFile
import storeFile
import rowCount
import colCount
import bfsDict
import bfsNode
import bfsShortPathFinder
import gridToCoordinateConversion
import dfsNode
import aStarNode

print ""
#print "**************************"
#print "WELCOME TO THE SEARCH GAME !!!! "
#print "**************************"
print ""

""" Use sys to read from command line """
#print "Step1: Get the input map file"
if len(sys.argv) < 2:
        print ""
	print "PLEASE ENTER A VALID INPUT BY SPECIFYING WHICH ALGORITHM TO BE IMPLEMENTED FOR THE SEARCH GAME IN THE BELOW COMMAND FORMAT:"
	print "python <<Main pgm Name>>.py <<map name>> <<algorithm type(B or D or A)>>"
	print ""
	sys.exit(0)

#print "Step2: Store the given file name and algrthm type"
filename=sys.argv[1]
if len(sys.argv) == 3:
        algthmtype=sys.argv[2]
        #print "algthmtype"
        #print algthmtype
        if algthmtype!= 'B' and algthmtype!= 'D' and algthmtype!= 'A':
                #print "in 1"
                print "PLEASE ENTER A VALID INPUT BY SPECIFYING WHICH ALGORITHM TO BE IMPLEMENTED FOR THE SEARCH GAME IN THE BELOW COMMAND FORMAT:"
                print "python <<Main pgm Name>>.py <<map name>> <<algorithm type(B or D or A)>>"
                sys.exit(0)
else:
     #print "in 2"
     print "PLEASE ENTER A VALID INPUT BY SPECIFYING WHICH ALGORITHM TO BE IMPLEMENTED FOR THE SEARCH GAME IN THE BELOW COMMAND FORMAT:"
     print "python <<Main pgm Name>>.py <<map name>> <<algorithm type(B or D or A)>>"
     sys.exit(0)
#print "algthmtype"+algthmtype


#print "Step3: Call the read input file module"
print ""
rdFl=readFile.readFile()
rdFl.readInputFile(filename)

#print "Step4: Call the row count module"
print ""
rwCntFl=rowCount.rowCount()
rowCount=rwCntFl.getRowCnt(filename)

#print "Step5: Call the col count module"
print ""
colCntFl=colCount.colCount()
colCount=colCntFl.getColCnt(filename)

#print "Step6: Store the input file data in List module"
print ""
linelist=list();
stFl=storeFile.storeFile()
linelist=stFl.storeFileData(filename)
#print "Data received from Input File Data Module"
#for line in linelist:   
       #print line

#print "Step7: Store the given state information in a dictionary"
dicRef=bfsDict.bfsDict()
dictData={}
dictData=dicRef.getDictData(linelist)

#print "Data Dictionary key: "
#print dictData.keys()
print ""


if algthmtype=="B":
        #print "Step8: Call the breadth first search algorithm module"
        bfsPath=[]
        nodeRef=bfsNode.bfsNode()
        bfsPath=nodeRef.bfsAlgo(dictData,colCount,rowCount)
        #print bfsPath

        #print "Step9: End of BFS Search"

        #print "Step10: Find the shortest path using BFS expanded"
        bfsShortPath=[]
        pthFndRef=bfsShortPathFinder.bfsShortPathFinder()
        bfsShortPath=pthFndRef.pathFinder(dictData,colCount,rowCount,linelist)


        #print ""
        #print "OUTPUT"
        #print "******"
        #print ""

        #print "AGENT PATH IN THE SEARCH GAME USING BFS ALGORITHM"
        #print bfsPath
        #print "AGENT SHORTEST PATH IN THE SEARCH GAME USING BFS ALGORITHM"
        #print bfsShortPath
        algoStr="BFS ALGORITHM"
        #print ""
        #print "VISITED : AGENT PATH IN SEARCH GAME USING "+algoStr+" IN COORDINATE VALUES:"
        #print ""
        print "Visited:"
        print ""
        coordRef=gridToCoordinateConversion.gridToCoordinateConversion()
        coordRef.coordinateConverter(dictData,colCount,rowCount,linelist,bfsPath,algoStr)
        #print ""
        #print "SHORT PATH : AGENT PATH IN SEARCH GAME USING "+algoStr+" IN COORDINATE VALUES:"
        print ""
        print "Best Way:"
        print ""
        coordRef=gridToCoordinateConversion.gridToCoordinateConversion()
        coordRef.coordinateConverter(dictData,colCount,rowCount,linelist,bfsShortPath,algoStr)
        
elif algthmtype=="D":
        #print "Step8: Call the depth first search algorithm module"
        #sys.exit(0)
        dfsPath=[]
        nodeRef=dfsNode.dfsNode()
        dfsPath=nodeRef.dfsAlgo(dictData,colCount,rowCount)
        #print dfsPath

        #print "Step9: End of DFS Search"

        #print ""
        #print "OUTPUT"
        #print "******"
        #print ""

        #print "AGENT PATH IN THE SEARCH GAME USING DFS ALGORITHM"
        #print dfsPath
        
        algoStr="DFS ALGORITHM"
        #print ""
        #print "VISITED : AGENT PATH IN SEARCH GAME USING "+algoStr+" IN COORDINATE VALUES:"
        #print ""
        print "Visited:"
        print ""
        coordRef=gridToCoordinateConversion.gridToCoordinateConversion()
        coordRef.coordinateConverter(dictData,colCount,rowCount,linelist,dfsPath,algoStr)
        print ""
elif algthmtype=="A":
        #print "Step8: Call the A* search algorithm module"
        aStarPath=[]
        anodeRef=aStarNode.aStarNode()
        aStarPath=anodeRef.aStarAlgo(dictData,colCount,rowCount,linelist)
        #print aStarPath

        #print "Step9: End of A* Search"

        #print ""
        #print "OUTPUT"
        #print "******"
        #print ""

        #print "AGENT PATH IN THE SEARCH GAME USING A* ALGORITHM"
        #print aStarPath
        
        algoStr="A* ALGORITHM"
        #print ""
        #print "VISITED : AGENT PATH IN SEARCH GAME USING "+algoStr+" IN COORDINATE VALUES:"
        #print ""
        print "Visited:"
        print ""
        coordRef=gridToCoordinateConversion.gridToCoordinateConversion()
        coordRef.coordinateConverter(dictData,colCount,rowCount,linelist,aStarPath,algoStr)
        print ""
else:
        print "PLEASE ENTER A VALID INPUT BY SPECIFYING WHICH ALGORITHM TO BE IMPLEMENTED FOR THE SEARCH GAME IN THE BELOW COMMAND FORMAT:"
        print "python <<Main pgm Name>>.py <<map name>> <<algorithm type(B or D or A)>>"







        
 
