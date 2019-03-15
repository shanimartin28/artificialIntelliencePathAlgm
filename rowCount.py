import sys

class rowCount:
    
    """Module used to get the row count"""
    def getRowCnt(self,filename):
            
            try:
                filename=filename+".txt"
                #print "Step4.1: Obtain the row count data:"+filename
                fin = open(filename, "r")
                
                #print "Step4.2: Read the map file data into a list"
                lineList = fin.readlines()
                rowCnt=lineList[1]
                #print "rowCnt: %s" %rowCnt
                fin.close()
            except IOError:
                print "Exception: File %s does not exist!" % filename

            #print "Step4.3: End of Row count Module"
            #print ""
                
            return rowCnt
    
