import json

def load_dict_from_file(dictionary): return json.load(open(dictionary,'r',encoding='utf-8')) # khoi tao tu dien

def EditDistDP(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    DP = [[0 for i in range(len1 + 1)]
             for j in range(2)];
 
    for i in range(0, len1 + 1):
        DP[0][i] = i

    for i in range(1, len2 + 1):
        for j in range(0, len1 + 1):
            if (j == 0):
                DP[i % 2][j] = i
            elif(str1[j - 1] == str2[i-1]):
                DP[i % 2][j] = DP[(i - 1) % 2][j - 1]
            else:
                DP[i % 2][j] = (1 + min(DP[(i - 1) % 2][j],
                                    min(DP[i % 2][j - 1],
                                  DP[(i - 1) % 2][j - 1])))
    return DP[len2 % 2][len1]

def check_miss_spell(str_input,dictionary): # Liet ke cac tu sai chinh ta trong chuoi dau vao
    output={}
    for i in str_input.split(" "):
        if len(i.strip(','))==2 and i[1].isdigit():
            pass
        else:
            for j in dictionary:
                if i.lower().startswith(j):
                    van=i[len(j):].strip(',')
                    if i[len(j):].strip(',') in dictionary[j]:
                        pass
                    else:
                        list_word=[]
                        min_dp=len(van)
                        for token in  sorted(dictionary[j]):
                            dp=EditDistDP(van,token)
                        # print(dp,i[0:len(j)]+token)
                            if dp < min_dp:
                                min_dp = dp
                                list_word=[]
                            if dp == min_dp:
                                list_word.append(i[0:len(j)]+token)
                        output[i]=list_word
                    break
    return output

def get_correction(str_input,dictionary):
    error=check_miss_spell(str_input,dictionary)
    # print(error)
    # s=open('log.txt','a',encoding='utf-8')
    # s.write("input  : " + str_input+'\n')
    dimension=[str_input]
    output={}
    for i in error:
        # print(i,":",error[i])
        temp=[]
        for token1 in error[i]:
            for status in dimension:                # print(status,i,token1)
                str_clone= status.replace(i,token1)
                temp.append(str_clone)
        dimension=temp
    count=1
    for i in dimension:
        # s.write('output'+str(count)+': '+i+'\n')
        count+=1

    # s.writelines("****\n")
    return dimension
if __name__ == '__main__':
    import time
    dictionary = load_dict_from_file('dict_am.json')

    start_time = time.time()
    s=open('test.txt','r',encoding='utf-8').read().split('\n')
    for i in s:
        get_correction(i,dictionary)
    print("--- %f seconds ---" % (time.time() - start_time))
