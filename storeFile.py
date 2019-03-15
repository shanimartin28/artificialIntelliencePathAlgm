import sys

class storeFile:
    
    """Module used to store data from the map file"""
    def storeFileData(self,filename):
            
            try:
                filename=filename+".txt"
                #print ""
                #print "Store Input File Data Module:"
                #print "Step6.1: Obtain the input map file data:"+filename
                fin = open(filename, "r")
                
                #print "Step6.2: Read the map file data into a list"
                lineList = fin.readlines()
                colCnt=lineList[0]
                rowCnt=lineList[1]
                wowwowlist =[]
                #print "colCnt: %s" %colCnt
                #print "rowCnt: %s" %rowCnt
                
                #print "Step6.3: Contents in line list"
                #for line in lineList:
                    #print line
                    
                #print "Step6.4: Use new list to remove the new line characters"

                #print "Step6.4.1: Processing performed to obtain the grid format with the free spaces also and removing col and row values"
                #wowwowlist =[]
                for line in lineList:
                        tempList=[]
                        #print "Initial val of tempList",tempList
                        stripline=line.rstrip('\n')
                        #print "stripline"+stripline
                    
                        tempList.extend(stripline)
                        #print "val of tempList after strip line"
                        #print tempList

                        length = len(tempList)
                        #print "len of current tempList",length
                        #print "colCnt",colCnt
                        if int(length) == int(colCnt):
                            #print tempList
                            #print "wow this is complete so add to wowow list- which is:"
                            wowwowlist.extend(tempList)
                            #print wowwowlist
                        else:
                            for j in range(1,int(length)+1):
                                #print "in j for"
                                ch=tempList[j-1]
                                #print "chars obtained:"+ch
                                if ch=="x" or ch==" " or ch=="s" or ch=="g" or ch=="f":
                                    #print "Continue with checking"
                                    flag=1
                                else:
                                    #print "DO NOT CHECK"
                                    #print "value of ch"+ch
                                    #tempList.remove[ch]
                                    flag=0
 
                            if flag == 1:
                                diff=int(colCnt)-int(length)
                                #print "diff",diff

                                if diff !=0 :
                                    for i in range(1,int(diff)+1):
                                        #print "hello there is a difference"
                                        #print "processed templist"
                                        tempList.extend("f")

                                #print "wow this is complete so add to wowow list- which is:"
                                wowwowlist.extend(tempList)
                                #print wowwowlist
             

                                

                #print "final list"
                #print wowwowlist
                                        
                #linelistNew=list();
                #for line in lineList:
                #    linelistNew.extend(list(line.rstrip('\n')));
                #print "Step6.5: New line list contents"
                #print wowwowlist
                #for line in linelistNew:   
                #    print line
                #fin.close()
                
                print ""     
            except IOError:
                print "Exception: File %s does not exist!" % filename

            
            #print "6.6: End of Store Input File Data Module"
            #sys.exit(0)
            #print ""
            return wowwowlist
    
