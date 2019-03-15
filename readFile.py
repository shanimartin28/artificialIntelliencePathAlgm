import sys

class readFile:
    
    """Module used to read from the map file"""
    def readInputFile(self,filename):
            
            try:
                filename=filename+".txt"
                #print ""
                #print "Read Input File Module:"
                #print "Step3.1: Reading the input map file:"+filename
                fin = open(filename, "r")
                str3 = fin.read()
                """Check1"""
                #print "Step3.2: Contents of whole file %s-" % filename
                #print str3
                fin.close()
                #print ""     
            except IOError:
                print "Exception: File %s does not exist!" % filename

            
            #print "3.3: End of Read Input File Module"
            #print ""
            return
    
