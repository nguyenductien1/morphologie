import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
import os.path

def getData(mot):
    #er => age r_post Nom:
    if os.path.exists('./cache/data_'+mot+'.txt'):
        return 1
    else:
        r = requests.get(f'http://www.jeuxdemots.org/rezo-dump.php?gotermsubmit=Chercher&gotermrel={mot}&rel=')
        soup = BeautifulSoup(r.text, 'html.parser')
        check = soup.find("div", {"class":"jdm-warning"})
        """
        check = str(check)
        check_condition = '<div class="jdm-warning"><br/>Le terme '+"'"+mot+"'"+ " n'existe pas !</div>"
        """
        
        if check:
            return -1
        else:
            code = soup.find('code')
            f = open('./cache/data_'+mot+'.txt', 'w')
            f.write(str(code))
            f.close()
            return 1


def filterData(mot,typeData, startLine, endLine):

    flist = open('./cache/data_'+mot+'.txt', 'r').readlines()
    parsing = False
    open(typeData + ".csv", "w").close()
    hs = open(typeData + ".csv",'a')
    for line in flist:
        if line.startswith(startLine):
            parsing = True
            continue
        elif line.startswith(endLine):
            parsing = False
            break
        if parsing:
            if line != "\n":
                hs.write(line)
    hs.close()



#Read as dataframe
def readAsDataFrame(file):
    f = open(file, "r")
    data = []
    for i, line in enumerate(f.readlines()): #Read each line as an object and count element
        splitted = line.split(";")
        data.append(splitted)
    df = pd.DataFrame(sorted(data, key=lambda row: len(row), reverse=True))
    return df

#Find an Entry have the research terme
def findNodeID2(mot, terme):
    check_mot = getData(mot)
    if check_mot == [-1]:
        return "'Le mot n'existe pas'"
    else:
        #NodesTypes
        filterData(mot,"NodesTypes","// les types de noeuds (Nodes Types) : nt;ntid;'ntname'\n","// les noeuds/termes (Entries) : e;eid;'name';type;w;'formated name' \n")
        #Entries
        filterData(mot,"Entries","// les noeuds/termes (Entries) : e;eid;'name';type;w;'formated name' \n","// les types de relations (Relation Types) : rt;rtid;'trname';'trgpname';'rthelp' \n")
        #RelationsTypes
        filterData(mot,"RelationsTypes","// les types de relations (Relation Types) : rt;rtid;'trname';'trgpname';'rthelp' \n","// les relations sortantes : r;rid;node1;node2;type;w \n")
        #RelationsSortants
        filterData(mot,"RelationsSortants","// les relations sortantes : r;rid;node1;node2;type;w \n","// les relations entrantes : r;rid;node1;node2;type;w \n")
        #RelationsEntrantes
        filterData(mot,"RelationsEntrantes","// les relations entrantes : r;rid;node1;node2;type;w \n","// END")
        df_Entries = readAsDataFrame("Entries.csv")
        foundEntry = df_Entries[lambda x: x[2]==terme]
        if len(foundEntry) > 0:
            #Get id of node
            node_ID = foundEntry[1].values[0]
            return node_ID
        else:
            return -1
#Find node in Relations Sortants

def findRelation2(nodeID):
    if nodeID != -1:
            df_RelationsSortants = readAsDataFrame('RelationsSortants.csv')
            foundRelation = df_RelationsSortants[lambda x: x[3]== nodeID]
            if len(foundRelation) == 0:
                return [-1]
            else:
                foundRelationID = foundRelation[4].values[0]
                df_RelationType = readAsDataFrame('RelationsTypes.csv')
                foundRelationType = df_RelationType[lambda x: x[1]== foundRelationID]
                return foundRelationType
    else:
        return [-1]



