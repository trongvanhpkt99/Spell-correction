import re
import time


def no_accent_vietnamese(s):
    s = re.sub(r'[àáạảã]', 'a', s)
    s = re.sub(r'[âầấậẩẫ]', 'â', s)
    s = re.sub(r'[ăằắặẳẵ]', 'ă', s)
    s = re.sub(r'[èéẹẻẽ]', 'e', s)
    s = re.sub(r'[êềếệểễ]', 'ê', s)
    s = re.sub(r'[òóọỏõ]', 'o', s)
    s = re.sub(r'[ơờớợởỡ]', 'ơ', s)
    s = re.sub(r'[ôồốộổỗ]', 'ô', s)
    s = re.sub(r'[ìíịỉĩ]', 'i', s)
    s = re.sub(r'[ùúụủũ]', 'u', s)
    s = re.sub(r'[ưừứựửữ]', 'ư', s)
    s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(r'[Đ]', 'D', s)
    s = re.sub(r'[đ]', 'd', s)
    return s

def load_word_dict(file_input):
    s=open(file_input,'r',encoding='utf-8').read().split('\n')
    diction={}
    for i in s:
        k= i.split(':')
        diction[k[0]]={j:j for j in k[1].split(',')}
    return diction
def check_spell(str_string,dictionary):
    str_input=no_accent_vietnamese(str_string)
    str_input=str_input.strip(',').lower()
    if not str_input.isdigit():
        for i in range(len(str_input)-1):
            if str_input[i+1] in dictionary[str_input[i]]: pass
            else :
                print(str_input[i],str_input[i+1]) 
                return str_string
    return ""
input_string ="nhà 20 ngõ 2 nguyễn Kánh toàn, quận Cầu G1ấy, thành phố Hà Nội"



start_time = time.time()
diction=load_word_dict('Dictionary/nguyenam.txt')
word=input_string.split()
x=[check_spell(i,diction) for i in word]

print(x)
print("--- %f seconds ---" % (time.time() - start_time))