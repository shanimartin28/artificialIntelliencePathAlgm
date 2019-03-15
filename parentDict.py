import bfsNode
import sys

class parentDict:
	"""Dictionary to store the Parent Data"""
	def storeParent(self,parentNodeId,childNode,parentDictData):
            

            #print "Step 7.2: Print the details obtained in parentDictData"
            #print "parentNodeId"
            #print parentNodeId
            #print "childNode"
            #print childNode
            #print "parentDictData"
            #print parentDictData
            
            #print "Step 7.3: Store the parent child details "

            
                
            parentDictData[childNode]=bfsNode.bfsNode()
            parentDictData[childNode].parentId=parentNodeId
            #parentDictData[childNode].childId=childNode
            #print "parentId= ", parentDictData[childNode].parentId
            #print "childId= ",parentDictData[childNode].childId
            #print "childId=",childNode
            #print "parentDictData"
            #print parentDictData
            #print "________________"
            
                    
                    
              
                
            #sys.exit(0)    
            #print "Step 7.4: End of Data Dictionary module "
            return parentDictData



