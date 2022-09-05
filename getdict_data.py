import os
import json
from tqdm import tqdm
path='tudien'
diction_am={}
for i in tqdm(os.listdir(path)):
    s=open(path+'\\'+i,'r',encoding='utf-8').read().split('\n')
    
    for line in s:
        words=line.lower().strip().split(' ')
        for word in words:
            # print(word)
            if word.isalpha():
                try:
                    if word[0: 2] in ["kh","ch","tr","qu","ph","gh",'th','gi','nh','ngh','ng']:
                        if word[0: 2] not in diction_am : 
                            
                            diction_am[word[0:2]]=[] 
                        if word[2:] not in diction_am[word[0:2]] and word[2:].isalpha():
                            diction_am[word[0: 2]].append(word[2:])
                    
                    if word[0] not in diction_am : 
                        diction_am[word[0]]=[]
                    if  word[1:] not in diction_am[word[0]] and word[1:].isalpha():
                        diction_am[word[0]].append(word[1:])
                except Exception as e: print(e)
    # print(i)
test_dict_list = sorted(list(diction_am.items()), key = lambda key : len(key[0]),reverse = True)
  
# reordering to dictionary
res = {ele[0] : ele[1]  for ele in test_dict_list}
json_object = json.dumps(res, indent=4,ensure_ascii=False)
 
# Writing to sample.json
with open("dict_am.json", "w",encoding='utf-8') as outfile:
        outfile.write(json_object)