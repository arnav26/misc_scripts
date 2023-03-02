import pandas as pd
import sys

#x = pd.read_csv("/Users/amehrotra/Downloads/SUR_078FFFbed_110142.txt", sep = "\t", usecols=[0,1,2,3])
x = pd.read_csv(sys.argv[1], sep = "\t", usecols=[0,1,2,3])
x.sort_values(by=["chr","start"],inplace=True)

threshold = int(sys.argv[2])

i = 0
lastline = False
cnvresults = []
while i <= x.shape[0]-1:
    if i == x.shape[0]-1:
        cnvresults.append([x.iloc[i,0],x.iloc[i,1],x.iloc[i,2], x.iloc[i,3]])
        i += 1
    else:
        if x.iloc[i,0] == x.iloc[i+1,0]:
            if x.iloc[i+1,1] - x.iloc[i,2] > threshold:
                cnvresults.append([x.iloc[i,0],x.iloc[i,1],x.iloc[i,2], x.iloc[i,3]])
                i += 1
                
            else:
                cnvstart = x.iloc[i,1]
                while (x.iloc[i,0] == x.iloc[i+1,0]) and (x.iloc[i+1,1] - x.iloc[i,2] < threshold):
                    if x.iloc[i,3] == x.iloc[i+1,3]:
                        cnvtype = x.iloc[i,3]
                    else:
                        cnvtype = "Mixed"
                    if i+1 == x.shape[0]-1:
                        lastline = True
                        break
                    else:
                        i += 1
                if lastline:
                    cnvend = x.iloc[i+1,2]
                    i += 1
                    lastline = False
                else:
                    cnvend = x.iloc[i,2]
                cnvresults.append([x.iloc[i,0],cnvstart,cnvend,cnvtype])
                i += 1  
                
        else:
            cnvresults.append([x.iloc[i,0],x.iloc[i,1],x.iloc[i,2], x.iloc[i,3]])
            i += 1
    

result = pd.DataFrame(cnvresults, columns = ['Chr','Start','End','Type'])
print(result)