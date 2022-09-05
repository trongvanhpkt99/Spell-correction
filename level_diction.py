import os
import json

def load_dict_by_level(lv1, lv2, lv3):
    diction = {}
    s1 = open(lv1, 'r', encoding='utf-8').read().split('\n')
    s2 = open(lv2, 'r', encoding='utf-8').read().split('\n')
    s3 = open(lv3, 'r', encoding='utf-8').read().split('\n')
    for i in range(len(s1)):
        if s1[i].lower() not in diction:
            diction[s1[i].lower()]={}
            diction[s1[i].lower()]["value"]=s1[i] 
        if s2[i].lower() not in diction[s1[i].lower()]:
            diction[s1[i].lower()][s2[i].lower()]={}
            diction[s1[i].lower()][s2[i].lower()]["value"]=s2[i]
        if s3[i].lower() not in diction[s1[i].lower()][s2[i].lower()]:
            diction[s1[i].lower()][s2[i].lower()][s3[i].lower()] ={}
        diction[s1[i].lower()][s2[i].lower()][s3[i].lower()]["value"] =s3[i]
             
                
    return diction
lv1='Dictionary/dict_thanhpho.txt'
lv2='Dictionary/dict_quanhuyen.txt'
lv3='Dictionary/dict_phuongxa.txt'
output=(load_dict_by_level(lv1,lv2,lv3))
json_object = json.dumps(output, indent=4,ensure_ascii=False,sort_keys=True)
with open("dict_level.json", "w",encoding='utf-8') as outfile:
        outfile.write(json_object)