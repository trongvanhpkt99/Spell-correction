def split_sentence(str_input):
    mark=str_input.lower().find('xã')
    if mark!=-1:
        print(str_input[0:mark])
        print(str_input[mark:])
        print(mark)
s=open('test.txt','r',encoding='utf-8').read().split('\n')
for i in s: split_sentence(i)