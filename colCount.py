import sys

class colCount:
    
    """Module used to get the col count"""
    def getColCnt(self,filename):
            
            try:
                filename=filename+".txt"
                #print "Step5.1: Obtain the col count data:"+filename
                fin = open(filename, "r")
                
                #print "Step5.2: Read the map file data into a list"
                lineList = fin.readlines()
                colCnt=lineList[0]
                #rowCnt=lineList[1]
                #print "colCnt: %s" %colCnt
                #print "rowCnt: %s" %rowCnt
                fin.close()
            except IOError:
                print "Exception: File %s does not exist!" % filename

            #print "Step5.3: End of Col count Module"
            #print ""
                
            return colCnt
    
