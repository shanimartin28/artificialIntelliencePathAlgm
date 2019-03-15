import bfsNode
import sys

class bfsDict:
	"""Dictionary to store the Given World Data"""
	def getDictData(self,linelist):
            
            #print "Step 7.1: Obtain a new dictionary "
            nodeDictData={}

            #print "Step 7.2: Obtain reference to bfsNode "
            nodeRef=bfsNode.bfsNode()
            
            #print "Step 7.3: Store the map file details form linelist to dictionary "

            #print "Step 7.3.1: Remove the row and col count values"
            nodeList=[]
            
            for i in range(1,len(linelist)+1):
                lineItemStr=linelist[i-1]
                #print "lineItemStr"+lineItemStr
                
                if lineItemStr=="x" or lineItemStr==" " or lineItemStr=="s" or lineItemStr=="g" or lineItemStr=="f":        
                        nodeDictData[i]=bfsNode.bfsNode()
                        nodeDictData[i].nodeId=i
                        #nodeDictData[i].nodeState=linelist[i-1]
                        if linelist[i-1] == "x":
                            nodeDictData[i].nodeState="x"
                        if linelist[i-1] == " ":
                            nodeDictData[i].nodeState="f"
                        if linelist[i-1] == "s":
                            nodeDictData[i].nodeState="s"
                        if linelist[i-1] == "g":
                            nodeDictData[i].nodeState="g"
                        #print "nodeId= ", nodeDictData[i].nodeId
                        #print "nodeState= "+nodeDictData[i].nodeState
                        #print "________________"

                else:
                        print ""
                                    
                
            #sys.exit(0)    
            #print "Step 7.4: End of Data Dictionary module "

            return nodeDictData



