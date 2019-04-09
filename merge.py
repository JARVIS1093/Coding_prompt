import os
import yaml
samefile=[]
def checkdir(path,filename):
        p=path.split("/")      
        if (not os.path.exists(path+"/"+filename)):
                return 
        else:
                newpath="/".join(p[1:len(p)-1])
                checkdir("/"+newpath,filename)
                samefile.append(path+"/"+filename)

def merging(samefile):
        if len(samefile)>1:
                for i in reversed(range(1,len(samefile))):
                        merge(samefile[i-1],samefile[len(samefile)-1])
        else:
            return
        

def merge(path1,path2):
        with open(path1) as f1:
                datamap1=yaml.safe_load(f1)
        with open(path2) as f2:
                datamap2=yaml.safe_load(f2)
        datamap=mergedict(datamap1,datamap2)
        with open(path2,'w') as f3:
                yaml.dump(datamap,f3,default_flow_style=False)
        
def mergedict(datamap1,datamap2):   
        totalkeys=set(list(datamap1.keys() )+list(datamap2.keys()))    
        for keys in totalkeys:
            if keys in datamap1 and keys in datamap2:
                if type(datamap1[keys])==type(datamap2[keys]):
                    if type(datamap1[keys])==dict:
                        datamap2[keys]= mergedict(datamap1[keys],datamap2[keys])
                    elif type(datamap1[keys])==str or type(datamap1[keys])==int or type(datamap1[keys])==float:
                        datamap2[keys]=datamap2[keys]
                    elif type(datamap1[keys])==list:
                        datamap2[keys]=datamap1[keys]+datamap2[keys]
                elif type(datamap1[keys])==dict and type(datamap2[keys])!=dict:
                    temp=datamap1[keys]
                    datamap2[keys]=[]
                    datamap2[keys].append(temp)
                    datamap2[keys].append(datamap2[keys])
                elif type(datamap2[keys])==dict and type(datamap1[keys])!=dict:
                    temp=datamap2[keys]
                    datamap2[keys]=[]
                    datamap2[keys].append(temp)
                    datamap2[keys].append(datamap1[keys])
                else :
                    temp=datamap2[keys]
                    datamap2[keys]=[]
                    datamap2[keys].append(temp)
                    datamap2[keys].append(datamap1[keys])
                    
            elif keys in datamap1 and keys not in datamap2:
                datamap2[keys]=datamap1[keys]
        return datamap2

a=input("Enter the file path")
b=a.split("/")
filename=b[len(b)-1]
path="/home/bhavya/"+"/".join(b[0:len(b)-1])
checkdir(path,filename)
merging(samefile)
if ( os.path.exists(a)):
    os.system("python -m pyaml "+a)
else:
        print("file doesn't exist")
