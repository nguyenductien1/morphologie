import json
import function
import convertir_mot

mot = input("Entrez le mot candidat: ")

relation = open('relation.json', 'r')
data = json.load(relation)

num_last_char = int(convertir_mot.get_number_last_char(mot))
if num_last_char == -1:
    print("Le terme de ce mot n'existe pas dans notre dictionaire")
def get_first_level(mot, num_last_char):
    return data[mot[-num_last_char]]
first_level = get_first_level(mot, num_last_char)


def get_second_level(first_level, second_condition):
    return first_level[second_condition]

def get_third_level(second_level, third_condition):
    return second_level[third_condition]

def get_fourth_level(third_level, fourth_condition):
    return third_level[fourth_condition]

def get_fifth_level(fourth_level, fifth_condition):
    return fourth_level[fifth_condition]

for k1,v1 in first_level.items():
    if function.getData(mot) == -1:
        print("Le mot ", mot, " n'existe pas")
        break
    lv2 = get_second_level(first_level, k1)
    for i in range(0, len(lv2)):

        for k2,v2 in lv2[i].items():
            nodeID = function.findNodeID2(mot, k2)
            #print("mot: ", mot, "terme: ", k2)
            #print("Node ID", nodeID)
            lv3 = get_third_level(lv2[i], k2)
            for j in range(0, len(lv3)):
                for k3,v3 in lv3[j].items():
                    relationType = function.findRelation2(nodeID)
                    #print("Relation: ", relationType)
                    lv4 = get_fourth_level(lv3[j], k3)
                    for k in range(0, len(lv4)):
                        for k4,v4 in lv4[k].items():
                            mot_derive = convertir_mot.mot_derive(mot, k3)
                            #nodeID_derive = function.findNodeID2(mot_derive, v4[k])
                            #print("mot derive: ", mot_derive, "terme derive: ", v4[k], "NodeID Derive: ", nodeID_derive)
                            lv5 = get_fifth_level(lv4[k], k4)
                            for l in range(0, len(lv5)):
                                if function.getData(mot_derive) == -1:
                                    print("Le mot dérivé ", mot_derive, " n'existe pas")
                                nodeID_derive = function.findNodeID2(mot_derive, lv5[l])
                                if nodeID_derive !=-1:
                                    print("mot derive: ", mot_derive, " | terme derive: ", v4[k], " | NodeID Derive: ", nodeID_derive)
                                    print(mot,"=>",mot_derive)