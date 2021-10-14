import collections
import json
from typing import Collection
import pandas as pd

in_file = open("pharses.json","r")
in_data = json.load(in_file)
pharses = in_data['data']
list_type = ["det","nom","pro","adj","vb"]
#List type of words
list_det = []; list_nom = []; list_pro = []; list_adj = []; list_vb  = []
#list of relations 
list_relation = []

for i in range(0, len(pharses)):
    list_type_tempo = []
    for j in range(0, len(pharses[i])):
        for k,v in pharses[i][j].items():
            list_type_tempo.append(v)
    relation_debut = "debut_" + list_type_tempo[0]
    relation_fin = list_type_tempo[len(list_type_tempo)-1] + "_fin"
    list_relation.append(relation_debut)
    list_relation.append(relation_fin)
    for j in range(0,len(list_type_tempo) - 1):
        relation = list_type_tempo[j] + "_" + list_type_tempo[j + 1]       
        list_relation.append(relation)

for j in range(0, len(pharses)):
    for m in range(0,len(pharses[j])):
        for k,v in pharses[j][m].items():
                if v == "det":
                    list_det.append(k)
                if v == "nom":
                    list_nom.append(k)
                if v == "pro":
                    list_pro.append(k)
                if v == "adj":
                    list_adj.append(k)
                if v == "vb":
                    list_vb.append(k)
            

def probab_calculate(list_in, type_in):
    occurrences = collections.Counter(list_in)
    dict_prob_words = []
    for k, v in occurrences.items():
        prob = v/len(list_in)
        list_tempo = {k+"_"+type_in:prob}
        dict_prob_words.append(list_tempo)
        print("n","(", k,"|",type_in,"):", prob)
    return dict_prob_words


def probab_relation_calculate(list_relation):
    occurrences = collections.Counter(list_relation)
    print("** Count number of relation by type of relation **")
    print(occurrences)
    relation_start_list = []
    relation_end_list = []
    for k in occurrences.keys():
        k_p = k.split('_')
        relation_start_list.append(k_p[0])
        relation_end_list.append(k_p[1])
    count_rela_start = collections.Counter(relation_start_list)
    print("** Relation start by **")
    print(count_rela_start)

    print("** Probability of relations **")
    dict_prob_relation = []
    for k, v in count_rela_start.items():
        total = 0
        for k1, v1 in occurrences.items():
            if k1.split('_')[0] == k:
                total = total + v1
        print("Total relation start by",k, ":", total)
        print("Probability: ")
        
        for k2, v2 in occurrences.items():
            if k2.split('_')[0] == k:
                new_rela_dict = {k2:v2/total}
                dict_prob_relation.append(new_rela_dict)
                print(k2, ":", v2/total)
    return dict_prob_relation


dict_word = []
print("PROBABILITY OF WORDS: ")

print("** det **")
dict_det = probab_calculate(list_det, "det")
dict_word.append(dict_det)

print("** nom **")
dict_nom = probab_calculate(list_nom, "nom")
dict_word.append(dict_nom)

print("** pro **")
dict_pro = probab_calculate(list_pro,"pro")
dict_word.append(dict_pro)
print("** adj **")
dict_adj = probab_calculate(list_adj, "adj")
dict_word.append(dict_adj)
print("** vb **")
dict_vb  = probab_calculate(list_vb, "vb")
dict_word.append(dict_vb)




print("PROBABILITE OF REALTIONS")
dict_prob_relation = probab_relation_calculate(list_relation)
#print(dict_prob_relation)
"""
print(dict_det)
print(dict_nom)
print(dict_pro)
print(dict_adj)
print(dict_vb)

pharse_in = ["la","petite","brise","la","glace"]
for i in range(0, len(pharse_in)):
    for j in range(0, len(dict_word)):
        for m in range(0, len(dict_word[j])):
            for k,v in dict_word[j][m].items():
                if k.split('_')[0] == pharse_in[i]:
                    



data = {'type':list_type, "la":[1,2,3,4,5]}

df = pd.DataFrame(data)
print(df)
"""


