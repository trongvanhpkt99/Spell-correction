import json
import check_misspell
import  dict_correction
def load_dict(json_dict):
    return json.load(open(json_dict,'r',encoding='utf-8'))

def correct(str_input):
    arr=dict_correction.get_err_from_str(str_input,diction)
    # print(arr)
    output=[]
    for i in arr:
        x=check_misspell.get_correction(i,dict_am)
        # print(x)
        flag=False
        for j in x:
            if j.strip().lower() in diction:
                # print(j.strip())
                output.append(j.strip())
                flag=True
                break
        if not flag:
            output.append(i.strip())
    try:
        # print(str_input)
        sub=output[len(output)-3:]
        # print(output[len(output)-3:])
        # print(sub)
        tp=dict_correction.dict_correction(sub[2],dict_level)
        qh=dict_correction.dict_correction(sub[1],dict_level[tp.lower()])
        px=dict_correction.dict_correction(sub[0],dict_level[tp.lower()][qh.lower()])
        # print(px,qh,tp)
        output=output[0:len(output)-3]+[px,qh,tp]
        # print(json.dumps(dict_level[tp.lower()][qh.lower()], indent=4,ensure_ascii=False))
    except Exception as e:
        # print(e)
        pass
    return (", ".join(output))
input_str="Thôn Đông Ngân, xã Đông Hôi, huyện Đông Anh, Thành phố Hà Nội"

dict_am=load_dict('dict_am.json')
dict_level=load_dict('dict_level.json')
diction=dict_correction.load_dict('Dictionary/dict_tonghop.txt')

import time
a=open('out.txt','a',encoding='utf-8')
s=open('test.txt','r',encoding='utf-8').read().split('\n')
for i in s:
    i=i.strip('.')
    start_time = time.time()
    print("input:  "+i)
    a.write("input:  "+i+'\n')
    print("output: "+correct(i))
    a.write("output: "+correct(i)+'\n')
    print("--- %s seconds ---" % (time.time() - start_time))
